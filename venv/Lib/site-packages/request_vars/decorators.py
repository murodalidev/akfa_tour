from functools import wraps

from request_vars.utils import get_variable, set_variable


__all__ = ['request_cache']


def request_cache(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        name = 'rc_{}.{}'.format(func.__module__, func.__name__)
        cached = get_variable(name)
        if cached:
            return cached
        result = func(*args, **kwargs)
        # Avoid cache forever in tasks, shell or tests.
        if get_variable('request'):
            set_variable(name, result)
        return result
    return wrapped
