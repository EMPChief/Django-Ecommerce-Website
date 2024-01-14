from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
# Import your apps' urls properly

urlpatterns = [
    path('', include('mainpage.urls')),
    path('', include('cart.urls')),
    path('order/', include('order.urls')),
    path('', include('product.urls')),
    path('', include('accounts.urls')),
    re_path(r'^grappelli/', include('grappelli.urls')),  # Assuming 'grappelli.urls' is correct
    path('admin/', admin.site.urls),
    # For filebrowser, ensure you are including it correctly as per the documentation
    # Example: path('filebrowser/', include('filebrowser.urls')), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
