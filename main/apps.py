from django.apps import AppConfig
from django.contrib.auth import get_user_model

class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        import main.signals





class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("kooner", "admin@example.com", "kooner@45")
