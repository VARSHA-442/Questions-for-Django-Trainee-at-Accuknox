# from django.db import transaction
# from .models import Order

# def test_signal_and_transaction():
#     try:
#         with transaction.atomic():  # Start a database transaction
#             order = Order.objects.create(product_name='Test Product')
#             print("Order created")
#             raise Exception("Simulated error to roll back transaction")
#     except Exception as e:
#         print(f"Exception caught: {e}")

#     # Check if the order was saved or rolled back
#     order_in_db = Order.objects.filter(product_name='Test Product').exists()
#     order_processed_in_db = Order.objects.filter(status='Processed by signal').exists()

#     print("Order with initial status in DB:", order_in_db)
#     print("Order with 'Processed by signal' status in DB:", order_processed_in_db)

from django.shortcuts import render

