from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.contrib.auth import views as auth_views

admin.autodiscover()
app_name = "foodcateringapp"
urlpatterns = [
    path("", views.mainIndex, name="mainindex"),
    path("foodmenu/", views.foodmenu, name="foodmenu"),
    path("addFoodMenu/", views.addFoodMenu, name="addFoodMenu"),
    path("checkout/", views.checkout, name="checkout"),
    path("checkoutcopy/", views.checkoutcopy, name="checkoutcopy"),
    path("editcart/", views.editcart, name="editcart"),
    path("editmenu/", views.editmenu, name="editmenu"),
    path("editmenuindex/", views.editmenuindex, name="editmenuindex"),
    path("adminindex/", views.adminIndex, name="adminindex"),
    path("admintest/", views.adminTest, name="admintest"),
    path("trackorderindex/", views.trackOrderIndex, name="trackorderindex"),
    path('api/orders/', views.get_orders, name='api/orders'),
    path("foodmenu/<int:menu_id>/",
         views.food_menu_detail, name="food_menu_detail"),
    path("orderdisplay/", views.displayorder, name="orderdisplay"),
    path("savepaymentdetails/", views.savepaymentdetails,
         name="savepaymentdetails"),
    path("saveshippingaddress/", views.saveshippingaddress,
         name="saveshippingaddress"),
    path("foodcart/", views.foodcart, name="foodcart"),
    path("foodmenu/<int:menu_id>/",
         views.food_menu_detail, name="food_menu_detail"),
    path('fooditemsold/', views.food_item_sold, name='fooditemsold'),
    path('membership/', views.membership_page, name='membership_page'),
    path(
        "increase-cart-item/<int:product_id>/",
        views.increase_cart_item,
        name="increase-cart-item",
    ),
    path(
        "decrease-cart-item/<int:product_id>/",
        views.decrease_cart_item,
        name="decrease-cart-item",
    ),
    path("add-to-cart/<int:item_id>/", views.add_to_cart, name="add-to-cart"),
    path("placeorder/", views.place_order, name="placeorder"),
    path(
        "get_updated_total_price/", views.get_updated_total_price, name="gettotalprice"
    ),
    path("viewchart/", views.chart_view, name="viewchart"),
    path("viewgraph/", views.graph_view, name="viewgraph"),
    path(
        "get_updated_total_price/", views.get_updated_total_price, name="gettotalprice"
    ),
    path(
        "update_order_status/<int:order_id>/",
        views.update_order_status,
        name="update_order_status",
    ),
    path("profile/", views.profilePage, name="profile"),
    # path("eventPage/", views.eventPage, name="eventPage"),
    path('cateringsets/', views.display_catering_sets, name="cateringsets"),
    path('booking/', views.booking, name="booking"),
    path("bookingcart/<int:booking_id>/", views.make_booking , name="makebooking"),
    # path("editbooking/<int:booking_id>/", views.edit_booking, name="editbooking"),
    path('book/<int:catering_set_id>/', views.book, name="book"),
    path('update_name/', views.update_name, name='update_name'),
    path('update_email/', views.update_email, name='update_email'),
    path('update_phone/', views.update_phone, name='update_phone'),
    path('update_image/', views.update_profile_image,
         name='update_profile_image'),
    path('edit_shipping_address/<int:address_id>/',
         views.edit_shipping_address, name='edit_shipping_address'),
    path('edit_payment/<int:card_id>/',
         views.edit_payment, name='edit_payment'),
    path('change_password/', views.change_password_view, name='change_password'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html'), name='password_change'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
