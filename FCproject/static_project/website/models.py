from django.db import models

class FoodMenu(models.Model):
    name = models.CharField(max_length=99)
    desciption = models.CharField(max_length=200)
    number_of_items = models.IntegerField()

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=99)
    food = models.CharField(max_length=99)
    beverage = models.CharField(max_length=99)
    price = models.FloatField(max_length=3)

    def __str__(self):
        return self.name