from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

User = get_user_model()

@receiver(post_migrate)
def create_default_admin(sender, **kwargs):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            password="Admin123@",
            email="admin@example.com"
        )
        print("✔ Admin user created automatically.")
