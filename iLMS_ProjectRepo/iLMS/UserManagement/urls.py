from django.urls import path
from UserManagement import views as user_views

urlpatterns = [
    path('', user_views.user_test, name='user_test'),
]
