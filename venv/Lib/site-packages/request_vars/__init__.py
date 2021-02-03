from threading import local


__version__ = '1.0.1'
default_app_config = 'request_vars.apps.RequestVarsConfig'

REQUEST_VARS = local()
