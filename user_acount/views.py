from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def handle_login(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            if not User.objects.filter(email=email).exists():
                messages.error(request, "Invalid email")
                return redirect('handle_login')

            if not email:
                messages.warning(request, 'Please enter email')
                return redirect('handle_login')

            if not password:
                messages.warning(request, 'Please enter password')
                return redirect('handle_login')

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'User logged in successfully')
                return redirect('dashboard/index')  
            else:
                messages.error(request, 'Invalid login credentials')

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    return render(request, 'login_page/login.html')  


