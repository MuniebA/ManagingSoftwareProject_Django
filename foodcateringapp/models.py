from django.db import models
from django.utils import timezone
from users.models import CustomUser

# from .models import Order, FoodItem
from django.apps import apps

# Order = apps.get_model('foodcateringapp', 'Order')


# Create your models here.


class FoodMenu(models.Model):
    # foodMenuID = models.AutoField(primary_key=True, editable=False, null='False')
    name = models.CharField(max_length=99, default="")
    description = models.CharField(max_length=200, default="")

    categories = models.CharField(
        max_length=99,
        choices=[
            ("Breakfast Set", "Breakfast Set"),
            ("Lunch Set", "Lunch Set"),
            ("Dinner Set", "Dinner Set"),
        ],
        default="",
    )

    foodmenuImage = models.ImageField(upload_to="Image/", default="")

    featured = models.CharField(
        max_length=99, choices=[("Yes", "Yes"), ("No", "No")], default=""
    )

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    # foodItemID = models.AutoField(primary_key=True, editable=False, null='False')
    name = models.CharField(max_length=99, default="")
    description = models.CharField(max_length=200, default="")
    price = models.FloatField(max_length=8, default="0.00")
    foodmenu = models.ForeignKey(FoodMenu, on_delete=models.CASCADE)
    fooditemImage = models.ImageField(upload_to="Image/", default="")

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.food_item.name}"


class Order(models.Model):
    STATUS_CHOICES = [
        ("Preparing", "Preparing"),
        ("Out of kitchen", "Out of kitchen"),
        ("Delivering", "Delivering"),
        ("Success", "Success"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=99, choices=STATUS_CHOICES, default="Preparing"
    )
    total_price = models.FloatField(default=0)

    def __str__(self):
        return f"Order {self.id}"


# class User(models.Model):
#     username = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.EmailField()

#     def _str_(self):
#         return self.username


class Card(models.Model):
    card_number = models.BigIntegerField()
    expiry_date = models.DateField()
    cvc = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Card ending in {str(self.card_number)[-4:]}"


class ShippingAddress(models.Model):
    name = models.CharField(max_length=255, default="")
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    postal = models.IntegerField()
    city = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Shipping Address for {self.user.username}"


class Transaction(models.Model):
    payment_method = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total = models.FloatField(default=0)

    def __str__(self):
        return f"Transaction ID {self.id}"


class OrderItem(models.Model):
    fooditem = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"Order ID {self.id}"


class Event(models.Model):
    eventname = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField()
    location = models.CharField(max_length=100)
    eventImage = models.ImageField(upload_to="Image/", default="")

    def __str__(self) -> str:
        return f"Event ID {self.id}"


class CateringSet(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='catering_sets/', blank=True)
    description = models.TextField(blank=True)
    items = models.ManyToManyField(
        FoodItem, through='CateringSetItem', related_name="set_items")

    def total_price(self):
        total = sum(item.quantity *
                    item.food_item.price for item in self.set_items.all())
        return total

    def __str__(self):
        return self.name


class CateringSetItem(models.Model):
    catering_set = models.ForeignKey(
        CateringSet, on_delete=models.CASCADE, related_name='set_items')
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Booking(models.Model):
    # Link the booking to the user
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Link the booking to the catering set
    catering_set = models.ForeignKey(CateringSet, on_delete=models.CASCADE)
    date = models.DateField()  # Date of the booking
    time = models.TimeField()  # Time of the booking
    # Additional information (optional)
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.catering_set.name} - {self.date}"

    class Meta:
        verbose_name_plural = "Bookings"


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=15, blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="Image/", default="")

# custom middlewares
