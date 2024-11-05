from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserRegistrationForm, CustomLoginForm


def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        print("form was submitted")
        print(form.errors)
        if form.is_valid():
            print("form is valid")
            user = form.save()
            # Log the user in and redirect to the desired page
            login(request, user)  # the default login can still work
            return redirect('foodcateringapp:mainindex')
    else:
        form = CustomUserRegistrationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def custom_login(request):
    error_message = ""
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return redirect('foodcateringapp:foodmenu')
                # Check the user's type and redirect accordingly
                user_type = user.user_type
                if user_type == 'client':
                    return redirect('foodcateringapp:mainindex')
                elif user_type == 'operator':
                    return redirect('foodcateringapp:orderdisplay')
                elif user_type == 'admin':
                    return redirect('admin_login')

        else:
            # Form data is not valid, show an error message
            error_message = "Invalid username or password."

    else:
        # This is a GET request, show the login form
        form = CustomLoginForm()

    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/login.html', context)
