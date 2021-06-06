from django.shortcuts import render
from .models import Sleep
from sleep.serializers import SleepSerializer
from rest_framework import viewsets, permissions
# Create your views here.


# create new sleep
class SleepViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = SleepSerializer

#get all of the user's sleeps
    def get_queryset(self):
        return self.request.user.Sleep.all()
    
#save the the request to the user upon creation
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

