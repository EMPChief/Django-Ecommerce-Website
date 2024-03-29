from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import frontpage, shop


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
