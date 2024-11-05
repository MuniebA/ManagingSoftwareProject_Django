from django import forms
from .models import CustomUser  # Import my custom user model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']  # Add any additional fields you want in the form
        # widgets = {
        #     'user_type': forms.Select(attrs={'class': 'custom-select'})  # Add a custom CSS class
        # }

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'user_type')

# class CustomUserAdminForm(UserCreationForm):
#     user_type = CustomUser.user_type
#     class Meta:
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields
#         fields += ('user_type',)