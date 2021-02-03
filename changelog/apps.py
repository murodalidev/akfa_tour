from django.apps import AppConfig


class ChangelogConfig(AppConfig):
    name = 'changelog'

    def ready(self):
        import changelog.signals