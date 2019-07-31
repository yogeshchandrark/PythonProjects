from rest_framework import serializers
from employee.models import Profile
from django.contrib.auth.models import User

class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        #fields = '__all__'
        fields = ( 'first_name', 'last_name', 'email', 'url')
