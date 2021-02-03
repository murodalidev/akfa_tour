import time
import json
import datetime

from changelog.middleware import LoggedInUser
from changelog.models import ChangeLog, ACTION_CREATE, ACTION_UPDATE, ACTION_DELETE
from changelog.mixins import ChangeloggableMixin


def journal_save_handler(sender, instance, created, **kwargs):
    if isinstance(instance, ChangeloggableMixin):
        loggedIn = LoggedInUser()
        last_saved = get_last_saved(loggedIn.request, instance)
        changed = merge(last_saved['changed'], instance.get_changed_fields())
        if changed:
            changed = json.loads(json_dumps(changed))
            if created:
                ChangeLog.add(instance, loggedIn.current_user, loggedIn.address, ACTION_CREATE, changed,
                              id=last_saved['id'])
            else:
                ChangeLog.add(instance, loggedIn.current_user, loggedIn.address, ACTION_UPDATE, changed,
                              id=last_saved['id'])


def journal_delete_handler(sender, instance, using, **kwargs):
    if isinstance(instance, ChangeloggableMixin):
        loggedIn = LoggedInUser()
        last_saved = get_last_saved(loggedIn.request, instance)
        ChangeLog.add(instance, loggedIn.current_user, loggedIn.address, ACTION_DELETE, {}, id=last_saved['id'])


def json_dumps(value):
    return json.dumps(value, default=json_handler)


def json_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    return repr(x)


_last_saved = {}


def get_last_saved(request, instance):
    last_saved = _last_saved[request] if request in _last_saved else None
    if not last_saved or last_saved['instance'].__class__ != instance.__class__ or last_saved[
        'instance'].id != instance.id:
        last_saved = {
            'instance': instance,
            'changed': {},
            'id': None,
            'timestamp': time.time()
        }
        _last_saved[request] = last_saved
    return last_saved


def merge(o1, o2):
    for key in o2:
        val2 = o2[key]
        if isinstance(val2, dict) and key in o1:
            val1 = o1[key]
            for k in val2:
                val1[k] = val2[k]
        else:
            o1[key] = val2
    return o1
