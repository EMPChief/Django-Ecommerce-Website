# admin.py
from django.contrib import admin
from django import forms  # Import forms module
from ckeditor.widgets import CKEditorWidget  # Import CKEditorWidget
from .models import Product, Review

# Define a custom form with CKEditorWidget for rich text fields
class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Product
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Review
        fields = '__all__'

# Register your models with the custom form
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
