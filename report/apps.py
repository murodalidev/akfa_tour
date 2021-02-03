from django.apps import AppConfig


class ReportConfig(AppConfig):
    name = 'report'

    def ready(self):
        import report.signals
