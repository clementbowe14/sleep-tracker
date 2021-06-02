from django.shortcuts import render
from sleep.models import sleep
from sleep.serializers import SleepSerializer
from rest_framework import generics
# Create your views here.


# create new sleep
class SleepList(generics.ListCreateAPIView):
    queryset = Sleep.objects.all()
    seriliazer_class = SleepSerializer

class SleepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer

