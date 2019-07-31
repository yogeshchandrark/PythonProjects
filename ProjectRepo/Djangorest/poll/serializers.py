from rest_framework import serializers
from poll.models import Question, Choice
from django.contrib.auth.models import User

class pollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'
        #fields = ( 'first_name', 'last_name', 'email', 'url')
