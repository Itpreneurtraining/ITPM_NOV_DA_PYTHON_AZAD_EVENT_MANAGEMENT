from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "Account created successfully")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
        return redirect('register')

    return render(request, 'reg.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login successful")
            next_url = request.GET.get('next') or 'home'
            return redirect('index')
        else:
            messages.error(request, "username or password is incorrect")
            return redirect('login')

    return render(request, 'log.html')


from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

def logout_view(request):
    # Log the user out
    logout(request)
    
    # Add a success message
    messages.success(request, "You have logged out successfully.")
    
    # Redirect to the index page
    return redirect('index')



@login_required(login_url='login')
def book_event(request):
    # Booking logic here
    return render(request, 'book_event.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def my_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

