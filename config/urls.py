from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainpage.views import frontpage, shop, signup, login_new, custom_logout, custom_login
from product.views import product
from django.contrib.auth import views
from cart.views import add_to_cart

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('signup/', signup, name='signup'),
    path('logout/', custom_logout, name='logout'),
    path('login/', custom_login, name='login'),
    path('shop/<slug:slug>/', product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
