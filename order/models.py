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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_email = models.CharField(max_length=255)
    order_first_name = models.CharField(max_length=100, blank=True, null=True)
    order_last_name = models.CharField(max_length=100, blank=True, null=True)
    order_address = models.CharField(max_length=255)
    order_city = models.CharField(max_length=100)
    order_phone_number = models.CharField(max_length=15, blank=True, null=True)
    order_state_province = models.CharField(max_length=100)
    order_zip_postal_code = models.CharField(max_length=12)
    order_country = models.CharField(max_length=50)
    order_created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    order_phone = models.CharField(max_length=15, blank=True, null=True)
    payment_intent = models.CharField(max_length=255, blank=True, null=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, default=PENDING, choices=ORDER_STATUS)
    def get_order_total(self):
        total = sum(item.get_total_price() for item in self.orderitem_set.all())
        return total
    class Meta:
        ordering = ['-order_created_at']

    def __str__(self):
        return f'Order ID: {self.id} | Name: {self.order_first_name} | Address: {self.order_address}, {self.order_city} | Country: {self.order_country} | Created at: {self.order_created_at}, Status | {self.status}'


class OrderItem(models.Model):
    order = models.ForeignKey(OrderMain, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'Order ID: {self.order.id} | Item: {self.quantity} x {self.product.name}'

    
    def get_total_price(self):
        return self.price * self.quantity
