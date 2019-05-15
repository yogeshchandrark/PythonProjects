from django.urls import path
from LabRequest import views as lab_views

urlpatterns = [

    path('', lab_views.lab_test, name='lab_test'),
]
