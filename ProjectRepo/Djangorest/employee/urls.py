from django.urls import path
from employee.views import *


urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('add/', employee_add, name="employee_add"),
]
