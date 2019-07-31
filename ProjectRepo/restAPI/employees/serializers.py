from rest_framework import serializers
from . models import employees

class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model=employees
#        fields=('firstname','Secondname')
        fields = '__all__'


class employeesListSerializer(serializers.ModelSerializer):

    class Meta:
        model=employees
        fields=('firstname',)
        # fields = '__all__'
