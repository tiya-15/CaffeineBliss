# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, OrderItem
from django.shortcuts import render, get_object_or_404
import json
def home(request):
    return render(request, 'index.html')

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
# coffee/views.py
def order_tracking(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'checkout.html', {'order': order})
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_success.html', {'order': order})
@csrf_exempt
def initiate_checkout(request):
    if request.method == 'POST':
        try:
            # Parse cart data from request
            data = json.loads(request.body)
            cart = data.get('cart', [])
            
            # Store cart in session
            request.session['cart'] = cart
            
            # Return redirect URL
            return JsonResponse({
                'redirect_url': reverse('checkout')
            })
            
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=400)
    
    return JsonResponse({
        'error': 'Invalid request method'
    }, status=405)

def checkout(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment')
        notes = request.POST.get('notes', '')
        
        # Get cart from session
        cart = request.session.get('cart', [])
        total = sum(float(item['price']) * int(item['quantity']) for item in cart) * 1.05
        
        # Create order
        order = Order.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            payment_method=payment_method,
            notes=notes,
            total_amount=total
        )
        
        # Add order items
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product_id=item['id'],
                product_name=item['name'],
                price=item['price'],
                quantity=item['quantity']
            )
        
        # Clear cart
        request.session['cart'] = []
        
        # Redirect to success page
        return redirect('order_success', order_id=order.id)
    
    # GET request - show checkout form
    cart = request.session.get('cart', [])
    if not cart:
        return redirect('home')
    
    subtotal = sum(float(item['price']) * int(item['quantity']) for item in cart)
    tax = subtotal * 0.05
    total = subtotal + tax
    
    return render(request, 'checkout.html', {
        'cart_items': cart,
        'subtotal': subtotal,
        'tax': tax,
        'total': total
    })