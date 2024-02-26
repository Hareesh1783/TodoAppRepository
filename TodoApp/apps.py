from django.apps import AppConfig

#if you want to create a app you should configure here

class TodoappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "TodoApp"
