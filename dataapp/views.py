from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm, UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home(request):
    # Renders the home page.
    return render(request, 'home.html')

def about(request):
    # Renders the about page.
    return render(request, 'about.html')

def user_login(request):
    # Handles user login.
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticates and logs in the user.
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('home')
        else:
            # Sends an error message if form is invalid.
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    # Handles new user registration.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Creates and authenticates new user.
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'], 
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        else:
            # Sends an error message if registration details are invalid.
            messages.error(request, "Invalid registration details.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

#@login_required
def add_service(request):
# Adds a new service associated with the logged-in user.
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            # Saves the new service and associates it with the user.
            service = form.save(commit=False)
            service.user = request.user
            service.save()
            messages.success(request, "Service added successfully.")
            # Redirect back to the current page or a specific page.
            return redirect('add_service')  # Adjust 'add_service' to your desired page
        else:
            # Sends an error message if form submission fails.
            messages.error(request, "Error in form submission.")
    else:
        form = ServiceForm()
    return render(request, 'add_service.html', {'form': form})
    