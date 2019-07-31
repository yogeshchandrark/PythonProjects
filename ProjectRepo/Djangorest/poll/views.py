from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from . serializers import pollSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from poll.models import *

class PollViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = pollSerializer

class PollList(APIView):

    def get(self, request):
        question = Question.objects.all()
        serializer = pollSerializer(question, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = pollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
def index(request):
    context = {}
    context['title'] = 'polls'
    return render(request, 'poll/index.html', context)


def poll(request, id=None):
    if request.method == "GET":
        try:
            question = Question.object.get(id=id)
        except:
            raise Http404

        context = {}
        context['question']= question
        return render(request, 'poll/poll.html', context)
