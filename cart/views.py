from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from django.contrib.auth.decorators import login_required
from product.models import Product
from accounts.models import UserProfile
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    context = {'cart': cart}
    return render(request, 'cart/menu_cart.html', context)


def cart(request):
    return render(request, 'cart/cart.html')

def update_cart(request, product_id, action):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    current_quantity = cart.get_item(product_id).get('quantity', 0)
    
    if action == 'increment':
        new_quantity = current_quantity + 1
    elif action == 'decrement':
        new_quantity = max(current_quantity - 1, 0)

    cart.add(product_id, new_quantity, update_quantity=True)



    quantity = cart.get_item(product_id)
    if quantity:
        quantity = quantity['quantity'] 

        item = {
            'product': {
                'id': product.id, 
                'name': product.name, 
                'image': product.image, 
                'get_thumbnail': product.get_thumbnail(), 
                'price': product.price
            },
            'total_price': (quantity * product.price),
            'quantity': quantity
        }
    else:
        item = None

    response = render(request, 'cart/menu_cart.html', {'cart': cart, 'item': item})
    response['HX-Trigger'] = 'update-menu-cart'
    return response

@login_required
def checkout(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'user_profile': user_profile}
    return render(request, 'cart/checkout.html', context)

def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')

def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')