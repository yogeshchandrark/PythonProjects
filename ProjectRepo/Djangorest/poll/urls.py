from django.urls import path
from poll.views import *

urlpatterns = [
    path('', index, name='poll_list'),
    path('<int:id>/', poll, name='single_poll'),
]
