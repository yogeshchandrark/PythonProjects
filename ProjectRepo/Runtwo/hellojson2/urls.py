from django.urls import path
from . import views

app_name = 'hellojson2'

urlpatterns = [
    path('', views.index, name='index'),
    path('getlist/', views.getlist, name='getlist'),
    path('senddata/', views.senddata, name='senddata'),
]
