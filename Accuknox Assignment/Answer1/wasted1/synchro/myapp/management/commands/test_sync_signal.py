from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Proves Django signals are synchronous'

    def handle(self, *args, **kwargs):
        self.stdout.write("Before user creation...")
        User.objects.create_user(username='testuser_sync', password='pass123')
        self.stdout.write("After user creation — only prints AFTER signal finishes.")
        self.stdout.write("This proves signals block the caller (synchronous).")
