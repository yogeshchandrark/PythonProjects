from django.urls import path
from Inventory import views as inventory_views

urlpatterns = [
    path('', inventory_views.inventory_test, name='inventory_test'),
]
