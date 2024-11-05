from django.apps import AppConfig


class FoodcateringappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foodcateringapp'

    def ready(self):
        import foodcateringapp.signals
