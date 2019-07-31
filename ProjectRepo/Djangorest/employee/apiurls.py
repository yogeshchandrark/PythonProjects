from django.contrib import admin
from django.urls import path, include
from employee.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', EmployeeViewSet)

urlpatterns = [
    path('employeesView/', include(router.urls)),
]
