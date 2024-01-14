from django.apps import AppConfig

class PersonalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal'

    def ready(self):
        # Импорт сигналов здесь, чтобы гарантировать, что приложения полностью загружены
        from . import signals