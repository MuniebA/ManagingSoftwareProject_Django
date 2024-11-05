from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
# Register your models here.

# admin.site.register(CustomUser)

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     fieldsets = UserAdmin.fieldsets + (
#         ('Custom Fields', {'fields': ('user_type',)}),
#     )
    
# admin.site.register(CustomUser, CustomUserAdmin)
class UserTypeFilter(admin.SimpleListFilter):
    title = 'User Type'
    parameter_name = 'user_type'

    def lookups(self, request, model_admin):
        return (
            ('operator', 'Operator'),
            ('client', 'Client'),
            ('admin', 'Admin'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'operator':
            return queryset.filter(user_type='operator')
        if self.value() == 'client':
            return queryset.filter(user_type='client')
        if self.value() == 'admin':
            return queryset.filter(user_type='admin')
        

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm  # Use the custom form for adding users

    list_filter = (UserTypeFilter, 'is_staff', 'is_superuser', 'is_active')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('user_type',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'user_type'),  # Specify the fields for adding users
        }),
    )

    def save_model(self, request, obj, form, change):
        if form.cleaned_data['user_type'] == 'admin':
            obj.is_superuser = True  # Set superuser status for admin users
            obj.is_staff = True  # Set staff status for admin users
        obj.save()

admin.site.register(CustomUser, CustomUserAdmin)