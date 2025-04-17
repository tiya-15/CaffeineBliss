# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

def home(request):
    return render(request, 'index.html')

# Define a view function for the login page
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
        
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')  # Redirect to root URL which is home
    
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('/')

# Define a view function for the registration page
def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Validate input
        if not (username and email and password):
            messages.error(request, "All fields are required!")
            return redirect('/signup/')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('/signup/')
            
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('/signup/')
        
        try:
            # Create new user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password  # create_user will hash the password automatically
            )
            messages.success(request, "Account created successfully! Please login.")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "An error occurred during registration. Please try again.")
            return redirect('/signup/')
    
    return render(request, 'signup.html')