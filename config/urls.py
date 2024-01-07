from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from cart.views import add_to_cart, cart, checkout
from mainpage.views import custom_login, custom_logout, frontpage, login_new, shop, signup
from product.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('signup/', signup, name='signup'),
    path('logout/', custom_logout, name='logout'),
    path('login/', custom_login, name='login'),
    path('shop/<slug:slug>/', product, name='product'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
