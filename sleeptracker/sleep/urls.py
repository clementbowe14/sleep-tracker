from django.urls import path
from sleep import views

urlpatterns = [
    path('sleep/', views.SleepList.as_view()),
    path('sleep/<int:pk>', views.SleepDetail.as_view()),
]