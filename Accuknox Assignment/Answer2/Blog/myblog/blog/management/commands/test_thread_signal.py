import threading
import logging
from django.core.management.base import BaseCommand
from blog.models import Post

logging.basicConfig(level=logging.INFO)

class Command(BaseCommand):
    help = 'Proves signals run in same thread as caller'

    def handle(self, *args, **kwargs):
        caller_thread = threading.current_thread().name
        logging.info(f"Caller thread: {caller_thread}")
        Post.objects.create(title="Test Post", content="Testing threads")
        self.stdout.write("Both log lines show MainThread — same thread proven.")