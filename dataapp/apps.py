from django.apps import AppConfig

class DataAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dataapp'

    def ready(self):
        # Here you can put application-specific startup code
        pass
