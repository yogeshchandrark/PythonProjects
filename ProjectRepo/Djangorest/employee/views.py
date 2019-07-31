from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from employee.forms import UserForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import employeesSerializer
from rest_framework import viewsets

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = employeesSerializer

def employee_list(request):
    context ={}
    context['users']= User.object.all()
    context['title']='Employees'
    return render(request, 'employee/index.html', context)

def employee_details(request, id=None):
    context={}
    context['users'] = get_object_or_404(User, id=id)
    return render(request, 'employee/details.html', context)

def employee_add(request):
    context = {}
    if request.method == "POST":
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/add.html', context)
    else:
        user_form = UserForm()
        context['user_form'] = user_form
        return render(request, 'employee/add.html', context)
