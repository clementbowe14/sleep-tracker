from django.shortcuts import render
from .models import Sleep
from rest_framework.authentication import TokenAuthentication
from sleep.serializers import SleepSerializer
from rest_framework import viewsets, permissions
# Create your views here.


# create new sleep
class SleepViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = SleepSerializer

#get all of the user's sleeps
    def get_queryset(self):
        return self.request.user.sleep.all()
    
#save the the request to the user upon creation
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

