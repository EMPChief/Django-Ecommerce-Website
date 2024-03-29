from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages


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
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


@login_required(login_url='login')
def custom_logout(request):
    logout(request)
    return redirect('frontpage')

@login_required(login_url='login')
def myaccount(request):
    return render(request, 'accounts/myaccount.html')

@login_required(login_url='login')
def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.emaIL = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        user.save()
        return redirect('myaccount')
        
    return render(request, 'accounts/edit_myaccount.html')