# store this as core/management/commands/create_superuser_if_none.py
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username=os.environ["SUPERUSER_NAME"],
                email=os.environ["SUPERUSER_EMAIL"],
                password=os.environ["SUPERUSER_PASSWORD"],
            )
