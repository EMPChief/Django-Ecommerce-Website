from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import custom_login, custom_logout, signup, myaccount


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', custom_logout, name='logout'),
    path('login/', custom_login, name='login'),
    path('myaccount/', myaccount, name='myaccount'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
