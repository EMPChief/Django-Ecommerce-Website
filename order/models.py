from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class OrderMain(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    PROBLEM = 'problem'
    PENDING = 'pending'
    ORDER_STATUS = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),
        (PROBLEM, 'Problem'),
        (PENDING, 'Pending'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order_email = models.CharField(max_length=255, null=True, blank=True)
    order_address = models.CharField(max_length=255, null=True, blank=True)
    order_city = models.CharField(max_length=100, null=True, blank=True)
    order_state_province = models.CharField(max_length=100, null=True, blank=True)
    order_zip_postal_code = models.CharField(max_length=12, null=True, blank=True)
    order_country = models.CharField(max_length=50, null=True, blank=True)
    order_created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, default=PENDING, choices=ORDER_STATUS)

    def __str__(self):
        return f'{self.order_address}, {self.order_city}, {self.order_state_province}, {self.order_zip_postal_code}, {self.order_country}'

class OrderItem(models.Model):
    order = models.ForeignKey(OrderMain, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
