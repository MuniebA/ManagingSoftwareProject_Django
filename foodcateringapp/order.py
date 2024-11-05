from django.db import models
from django.contrib.auth.models import User
from .models import Cart  # Replace '.models' with the actual path to your Cart model

from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    STATUS_CHOICES = (
        ('Preparing', 'Preparing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # Reference to the user's cart
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Preparing')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # You can add more fields as needed for your application, such as shipping information, delivery address, etc.
