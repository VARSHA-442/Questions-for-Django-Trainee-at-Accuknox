import threading
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post

logging.basicConfig(level=logging.INFO)

@receiver(post_save, sender=Post)
def notify_users(sender, instance, created, **kwargs):
    if created:
        signal_thread = threading.current_thread().name
        logging.info(f"Signal executed in thread: {signal_thread}")
        send_mail(
            subject='New Post Created',
            message=f'A new post titled "{instance.title}" has been created.',
            from_email='from@example.com',
            recipient_list=['user@example.com'],
        )