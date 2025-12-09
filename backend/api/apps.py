"""Apps for Task model."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Apps for Task."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
