from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Create default admin user if not exists"

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                "kooner",
                "admin@example.com",
                "Jass@78"
            )
            self.stdout.write(self.style.SUCCESS("Default admin created"))
        else:
            self.stdout.write("Admin user already exists")
