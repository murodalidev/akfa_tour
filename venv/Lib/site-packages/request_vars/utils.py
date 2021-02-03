from request_vars import REQUEST_VARS


__all__ = ['set_variable', 'get_variable', 'del_variable',
           'clear_thread_variable']


def set_variable(key, val):
    setattr(REQUEST_VARS, key, val)


def get_variable(key, default=None):
    return getattr(REQUEST_VARS, key, default)


def del_variable(key):
    if hasattr(REQUEST_VARS, key):
        del REQUEST_VARS.__dict__[key]


def clear_thread_variable():
    REQUEST_VARS.__dict__.clear()
