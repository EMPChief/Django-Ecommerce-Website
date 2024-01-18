from django.contrib import admin
from .models import Category, Product, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_display', 'price_cents', 'created_at')

    def price_display(self, obj):
        return f"${obj.price:.2f}"

    price_display.short_description = 'Price (Dollars)'

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)  # Register with the custom admin class
admin.site.register(Review)
