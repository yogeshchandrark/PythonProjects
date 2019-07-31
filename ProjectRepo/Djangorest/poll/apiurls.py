from django.contrib import admin
from django.urls import path, include
from poll.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', PollViewSet)

urlpatterns = [
    path('pollQuesView/', PollList.as_view()),
    path('pollView/', include(router.urls)),
]
