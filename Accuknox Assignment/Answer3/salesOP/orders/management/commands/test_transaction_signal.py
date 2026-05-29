from django.core.management.base import BaseCommand
from django.db import transaction
from orders.models import Order

class Command(BaseCommand):
    help = 'Proves signals run in same DB transaction as caller'

    def handle(self, *args, **kwargs):
        Order.objects.all().delete()  # Clean slate

        try:
            with transaction.atomic():
                order = Order.objects.create(product_name='Test Product')
                self.stdout.write("Order created inside transaction.")
                raise Exception("Simulated rollback error")
        except Exception as e:
            self.stdout.write(f"Exception caught: {e}")

        exists = Order.objects.filter(product_name='Test Product').exists()
        processed = Order.objects.filter(status='Processed by signal').exists()

        self.stdout.write(f"Order in DB after rollback: {exists}")
        self.stdout.write(f"Signal-processed order in DB: {processed}")
        self.stdout.write("Both are False — signal rolled back WITH the transaction.")