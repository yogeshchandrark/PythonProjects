"""iLMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from Inventory import views as inventory_views
from UserManagement import views as user_views
from LabRequest import views as lab_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inventory_views.inventory_test, name='inventory_test'),
    path('inventory/', include('Inventory.urls')),
    path('', user_views.user_test, name='user_test'),
    path('usermanagement/', include('UserManagement.urls')),
    path('', lab_views.lab_test, name='lab_test'),
    path('labrequest/', include('LabRequest.urls')),
]
