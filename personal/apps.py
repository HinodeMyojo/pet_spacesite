from django.apps import AppConfig
from . import signals


class PersonalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal'