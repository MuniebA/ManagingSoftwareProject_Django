from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foodcateringapp.urls')),
    path('users/', include('users.urls')),
    path('admin/login/', auth_views.LoginView.as_view(), name='admin_login')
]
