from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

User = get_user_model()

@receiver(post_migrate)
def create_default_admin(sender, **kwargs):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="kooner",
            password="Jass@45",
            email="koonerjatindersingh@gmail.com"
        )
        print("✔ Auto admin created.")
