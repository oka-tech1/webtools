from django.apps import AppConfig


class PcAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pc_app'

class PcAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pc_app'
    def ready(self):
        import pc_app.signals

class PcAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pc_app'
    def ready(self):
        import pc_app.signals
