from django.contrib import admin
from .models import OrderMain, OrderItem

class OrderItemInLIne(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_filter = ['status', 'order_created_at']
    search_fields = ['id', 'order_first_name', 'order_last_name', 'order_email', 'order_phone_number', 'order_address', 'order_city', 'order_zip_postal_code', 'order_country']
    inlines = [OrderItemInLIne]
    

admin.site.register(OrderMain, OrderAdmin)
admin.site.register(OrderItem)