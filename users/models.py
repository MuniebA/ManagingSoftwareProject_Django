from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    #define a constant(list) of choices
    USER_TYPE_CHOICES = [
        ('operator', 'Operator'),
        ('client', 'Client'),
        ('admin', 'Admin'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='client')

    # for membership
    membership_points = models.IntegerField(default=0)  # Level 0 as base membership
    tier = models.CharField(max_length=20, default="Entry")

    #method to increase membership based on spending
    def update_membership(self, amount_spent):
        # for every 100RM spent, increase membership level by 1
        self.membership_points += amount_spent // 20
        if (self.membership_points >= 2000):
            self.tier = "Diamond"
        elif (self.membership_points >= 1000):
            self.tier = "Gold"
        elif (self.membership_points >= 500):
            self.tier = "Silver"
        else:
            self.tier = "Entry"
        self.save()

    