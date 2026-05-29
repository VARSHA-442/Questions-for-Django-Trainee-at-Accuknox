from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def update_status_on_save(sender, instance, created, **kwargs):
    if created:  # Only run on first save, prevents recursion
        print("Signal handler called")
        Order.objects.filter(pk=instance.pk).update(status='Processed by signal')
        print("Status updated via signal")