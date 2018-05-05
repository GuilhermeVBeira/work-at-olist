from django.apps import AppConfig


class RecordConfig(AppConfig):
    name = 'apps.record'

    def ready(self):
        import apps.record.signals
