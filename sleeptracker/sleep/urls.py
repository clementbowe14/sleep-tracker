from rest_framework import routers
from django.urls import path
from sleep import views

router = routers.DefaultRouter()

urlpatterns = [
    path('sleep/', SleepViewSet, 'sleep'),
    path('sleep/<int:pk>', views.SleepDetail.as_view()),
]