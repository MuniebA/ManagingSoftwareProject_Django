from django.shortcuts import render
from .models import FoodItem

def foodmenu(request):
    return render(request, 'foodMenu.html', {})

def breakfast(request):
    all_items = FoodItem.objects.all
    return render(request, 'Breakfast.html', {'all':all_items})
