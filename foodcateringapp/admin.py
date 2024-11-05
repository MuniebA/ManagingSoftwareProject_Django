from django.contrib import admin
from django import forms

from .models import (
    FoodItem,
    FoodMenu,
    CartItem,
    Cart,
    Order,
    Card,
    ShippingAddress,
    Transaction,
    OrderItem,
    CateringSet,
    CateringSetItem,
    Booking,
    Event,
    UserProfile,
)

admin.site.register(Order)
admin.site.register(Card)
admin.site.register(ShippingAddress)
# admin.site.register(FoodItem)
# admin.site.register(FoodMenu)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(CateringSet)
admin.site.register(CateringSetItem)
admin.site.register(Booking)
admin.site.register(Event)
admin.site.register(UserProfile)


class DateRangeForm(forms.Form):
    start_date = forms.DateField(label="Start Date", required=False)
    end_date = forms.DateField(label="End Date", required=False)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    date_hierarchy = "date"  # Enable date drill-down
    # Customize displayed columns
    list_display = ("id", "date", "user", "total")
    list_filter = ("date",)  # Add filter for transaction date
    # actions = [filter_transactions_by_date_range]  # Include the custom action

    def changelist_view(self, request, extra_context=None):
        # Add the date range form to the change list view
        extra_context = extra_context or {}
        extra_context["date_range_form"] = DateRangeForm(request.GET)
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "foodmenu",
    )  # Customize displayed columns


@admin.register(FoodMenu)
class FoodMenuAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "categories",
        "featured",
    )  # Customize displayed columns


admin.site.site_header = "FoodEdge"
admin.site.index_title = "FECS Admin Dashboard"
