from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages


def custom_logout(request):
    logout(request)
    return redirect('frontpage')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('frontpage')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            return redirect('/')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request,'accounts/signup.html', context)


@login_required
def myaccount(request):
    return render(request, 'accounts/myaccount.html')