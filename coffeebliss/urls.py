"""coffeebliss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from coffee import views

#for API
from django.urls import path, include
from rest_framework import routers
from coffee import api


router = routers.DefaultRouter()
router.register(r'orders', api.OrderViewSet)
urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.register_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('order-success/<int:order_id>/', views.order_success, name='order_success'),
    path('initiate-checkout/', views.initiate_checkout, name='initiate_checkout'),
    path('checkout/', views.checkout, name='checkout'),

    #API ----
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
=======
from coffee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('signup/', register_page, name='signup'),
    path('logout/', logout_page, name='logout'),
>>>>>>> b17a32e964cc2db86b6c821185b65079e1521510
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
