from django.utils.module_loading import import_string

from request_vars.conf import settings
from request_vars.utils import clear_thread_variable, set_variable


class RequestVarsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        set_variable('request', request)
        set_variable('user', request.user)
        if settings.REQUEST_VARS_MIDDLEWARE_CALLBACK:
            import_string(settings.REQUEST_VARS_MIDDLEWARE_CALLBACK)(request)
        response = self.get_response(request)
        clear_thread_variable()
        return response

    def process_exception(self, request, exception):
        clear_thread_variable()
