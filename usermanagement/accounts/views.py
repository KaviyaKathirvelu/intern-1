# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomLoginForm
from django.contrib.auth.models import User  # Import User model

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)  # Get data from the form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard after login
            else:
                print("authentication failed")
        else:
            print(form.errors)
    else:
        form = CustomLoginForm()  # Create a new form instance for GET requests
    
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def dashboard_view(request):
    users = User.objects.all()  # Retrieve all users in the system
    return render(request, 'accounts/dashboard.html', {'users': users})  # Pass user data to the template

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout