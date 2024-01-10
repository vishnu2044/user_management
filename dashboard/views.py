from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    user = request.user
    print("user>>>>", user.username)
    print("user>>>>", user.email)
    
    if user:
        context = {
            user:user
        }
        return render(request, 'dashboard/index.html', context)
    else:
        return render(request, 'login_page/login.html') 


def user_profile(request):
    user = request.user
    print("user>>>>", user.username)
    print("user>>>>", user.email)
    if user:
        context ={
            user : user
        }
        return render(request, 'dashboard/user_profile.html', context)
    
    else:
        return render(request, 'login_page/login.html') 
    

def change_passwrod(request):
    print("its calling!!!!!!!!!!!!!!")
    try:    
        user = request.user
        if user.is_authenticated:
            if request.method == "POST":
                old_password = request.POST.get('old_password')
                new_password = request.POST.get('new_password')
                confirm_password = request.POST.get('confirm_password')
                

                if not user.check_password(old_password):
                    messages.error(request, 'please enter the correct password !')
                    return redirect(user_profile)
                
                if len(new_password) < 8:
                    messages.warning(request, 'password length must be greater than 8')
                    return redirect(user_profile)
                
                
                if old_password == new_password or old_password == confirm_password:
                    messages.warning(request, 'the new password is same as your old password please change')
                    return redirect(user_profile)

                if new_password != confirm_password:
                    messages.error(request, "Password mismatch")
                    return redirect(request, user_profile)

                user.set_password(new_password)
                user.save()
                auth.login(request, user)
                messages.success(request, "password changed successfully !")
                return redirect(user_profile)
            return redirect(request, user_profile)
        else:
            messages.error(request, 'You need to login first')
            return redirect('')
    except:
        return redirect('')
    

def logout_user(request):
    try:
        user = request.user
        if user.is_authenticated:
            logout(request)
        return redirect('handle_login')  
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return redirect('handle_login') 