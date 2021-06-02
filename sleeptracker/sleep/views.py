from django.shortcuts import render
from sleep.models import sleep
from sleep.serializers import SleepSerializer
from rest_framework import viewsets, permissions
# Create your views here.


# create new sleep
class SleepViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.isAuthenticated,
    ]
    serializer_class = SleepSerializer

#get all of the user's sleeps
    def get_queryset(self):
        return self.request.user.sleep.all()
    
#save the the request to the user upon creation
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#get detail of the sleeps
class SleepDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes[
        permissions.isAuthenticated,
    ]
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer

