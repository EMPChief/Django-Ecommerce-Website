from django.contrib import admin
from .models import OrderMain, OrderItem

admin.site.register(OrderMain)
admin.site.register(OrderItem)