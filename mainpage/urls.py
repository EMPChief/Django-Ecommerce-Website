from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import custom_login, custom_logout, frontpage, shop, signup


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('signup/', signup, name='signup'),
    path('logout/', custom_logout, name='logout'),
    path('login/', custom_login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
