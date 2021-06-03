from rest_framework import routers
from django.urls import path
from .views import SleepViewSet 


router = routers.DefaultRouter()
router.register(r'api/sleep', SleepViewSet, 'sleep')

urlpatterns = router.urls