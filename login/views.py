from functions.authentication import validate_user, user_auth
from django.shortcuts import render, redirect
from django.urls      import reverse
import time

# Create your views here.

def domain(request, *args, **kwargs):
    return redirect(reverse('login'))


def login(request, *args, **kwargs):
    if validate_user(request):
        return redirect(reverse('homepage'))
    else:
        if request.method == 'POST':
            time.sleep(1)
            if 'username' in request.POST and 'password' in request.POST:
                verified = user_auth(request.POST['username'], request.POST['password'])
                if verified:
                    response = redirect(reverse('homepage'))
                    response.set_cookie('user',request.POST['username'])
                    return response
                else:
                    ginger = {
                        'invalid_details': True,
                    }
                    return render(request, 'login.html', ginger)
            else:
                ginger = {
                    'invalid_details': True,
                }
                return render(request, 'login.html', ginger)
        else:
            ginger = {
                'invalid_details': False,
            }
            return render(request, 'login.html', ginger)


def logout(request, *args, **kwargs):
    response = redirect(reverse('login'))
    response.delete_cookie('user')
    return response
