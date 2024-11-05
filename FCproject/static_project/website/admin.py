from django.contrib import admin
from .models import FoodMenu
from .models import FoodItem

admin.site.register(FoodMenu)
admin.site.register(FoodItem)
