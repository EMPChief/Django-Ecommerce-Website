from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from ckeditor.widgets import CKEditorWidget
from django import forms

# Create your views here.


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    if request.method == 'POST':
        rating = request.POST.get('rating')
        content = request.POST.get('content', '')
        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)
            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                Review.objects.create(product=product, 
                                    rating=rating, 
                                    content=content, 
                                    created_by=request.user)
                return redirect('product', slug=slug)
    return render(request, 'product/product.html', context)


