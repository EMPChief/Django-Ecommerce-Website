from django.shortcuts import render
from .cart import Cart
from django.contrib.auth.decorators import login_required
# Create your views here.

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    context = {'cart': cart}
    return render(request, 'cart/menu_cart.html', context)


def cart(request):
    return render(request, 'cart/cart.html')

@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')


def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')