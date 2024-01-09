from django.shortcuts import render
from .models import order, OrderItem

# Create your views here.
def start_order(request):
    if request.method == 'POST':
        order_first_name = request.POST['first_name']
        order_last_name = request.POST['last_name']
        order_email = request.POST['email']
        order_phone = request.POST['phone']
        order_address = request.POST['address']
        order_zip_code = request.POST['zip_code']
        order_city = request.POST['city']
        order_state = request.POST['state']
        order_country = request.POST['country']
        
        order = Order.objects.create(.user, order_first_name=order_first_name)