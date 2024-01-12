from django.shortcuts import render, redirect
from .models import OrderMain, OrderItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
import json
import stripe
from django.conf import settings

@login_required 
def start_order(request):
    if request.method != 'POST':
        return redirect('cart')

    cart = Cart(request)
    data = json.loads(request.body)
    total_price = 0
    items = []

    for item in cart:
        product = item['product']
        total_price += product.price * int(item['quantity'])
        items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100)
            },
            'quantity': int(item['quantity']),
        })

    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url=request.build_absolute_uri('/cart/success/'),
        cancel_url=request.build_absolute_uri('/cart'),
    )
    payment_intent = session.payment_intent

    
    order = OrderMain.objects.create(
        user=request.user,
        order_first_name=data.get['order_first_name'],
        order_last_name=data.get['order_last_name'],
        order_phone=data.get['order_phone'],
        order_email= data.get['order_email'],
        order_address=data.get['order_address1'],
        order_city=data.get['order_city'],
        order_state_province=data.get['order_state_province'],
        order_zip_postal_code=data.get['order_zip_postal_code'],
        order_country=data.get['order_country'],
        payment_intent=payment_intent,
        paid=True,
        paid_amount=total_price,
    )

    for item in cart:
        product = item['product']
        quantity = int(item['quantity'])
        price = product.price * quantity
        OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
    cart.clear()

    return JsonResponse({'session': session, 'order': payment_intent})
