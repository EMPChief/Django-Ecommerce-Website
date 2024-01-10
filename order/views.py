from django.shortcuts import render, redirect
from .models import OrderMain, OrderItem
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required 
def start_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        order_first_name = request.POST.get('order_first_name')
        order_last_name = request.POST.get('order_last_name')
        order_email = request.POST.get('order_email')
        order_phone = request.POST.get('order_phone')
        order_address = request.POST.get('order_address1')
        order_zip_postal_code = request.POST.get('order_zip_postal_code')
        order_city = request.POST.get('order_city')
        order_state_province = request.POST.get('order_state_province')
        order_country = request.POST.get('order_country')
        order = OrderMain.objects.create(
            order_user=request.user,
            order_email=order_email,
            order_address=order_address,
            order_city=order_city,
            order_state_province=order_state_province,
            order_zip_postal_code=order_zip_postal_code,
            order_country=order_country,
        )
        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity
            item = OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
        return redirect('myaccount')
    return redirect('cart')
