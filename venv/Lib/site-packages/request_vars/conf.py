from django.conf import settings as dj_settings
from django.core.signals import setting_changed


DEFAULTS = {
    'REQUEST_VARS_MIDDLEWARE_CALLBACK': None
}


class Settings(object):
    def __getattr__(self, name):
        if name not in DEFAULTS:  # pragma: no cover
            msg = "'%s' object has no attribute '%s'"
            raise AttributeError(msg % (self.__class__.__name__, name))
        value = getattr(dj_settings, name, DEFAULTS[name])
        setattr(self, name, value)
        return value

    def change_setting(self, setting, value, enter, **kwargs):
        if setting not in DEFAULTS:  # pragma: no cover
            return

        if enter:
            setattr(self, setting, value)
        else:
            delattr(self, setting)


settings = Settings()
setting_changed.connect(settings.change_setting)
