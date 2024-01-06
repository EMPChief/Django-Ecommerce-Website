from django.shortcuts import render, redirect
from product.models import Product, Category
from django.db.models import Q
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth import logout, authenticate, login
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

    return render(request, 'mainpage/login.html')



def frontpage(request):
    products = Product.objects.all()[0:8]
    context = {'products': products}
    return render(request, 'mainpage/frontpage.html', context)


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
    return render(request,'mainpage/signup.html', context)




def login_new(request):
    return render(request,'mainpage/login.html')




def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    active_category = request.GET.get('category', '')

    if active_category:
        products = Product.objects.filter(category__slug=active_category)

    query = request.GET.get('query', '')
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'products': products,
        'categories': categories,
        'active_category': active_category
    }
    return render(request, 'mainpage/shop.html', context)
