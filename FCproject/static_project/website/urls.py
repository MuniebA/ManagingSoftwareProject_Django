from django.urls import path
from . import views

urlpatterns = [
    path('foodmenu/', views.foodmenu, name="foodmenu"),
    path('breakfast/', views.breakfast, name="breakfast")
]
