from django.shortcuts import render
from product.models import Product, Category
from django.db.models import Q






def frontpage(request):
    products = Product.objects.all()[0:8]
    context = {'products': products}
    return render(request, 'mainpage/frontpage.html', context)





def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    active_category = request.GET.get('category', '')

    if active_category:
        products = Product.objects.filter(category__slug=active_category)

    query = request.GET.get('query', '')
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'products': products,
        'categories': categories,
        'active_category': active_category
    }
    return render(request, 'mainpage/shop.html', context)
