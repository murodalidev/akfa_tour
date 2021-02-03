class Singleton(object):
    """Синглтон"""

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class LoggedInUser(Singleton):
    """Синглтон для хранения пользователя,
    от имени которого выполняется запрос"""
    __metaclass__ = Singleton

    request = None
    user = None
    address = None

    def set_data(self, request):
        self.request = id(request)
        if request.user.is_authenticated:
            self.user = request.user
            self.address = request.META.get('REMOTE_ADDR')

    @property
    def current_user(self):
        return self.user

    @property
    def have_user(self):
        return not self.user is None


class LoggedInUserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Инициализирует синглтон LoggedInUser
        """
        logged_in_user = LoggedInUser()
        logged_in_user.set_data(request)

        response = self.get_response(request)

        return response
