from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Sleep(models.Model):
    sleep_duration = models.IntegerField();
    owner = models.ForeignKey(
        User, related_name="sleep", on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)