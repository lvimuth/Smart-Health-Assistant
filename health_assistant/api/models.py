from django.db import models

# Create your models here.
# api/models.py
from django.contrib.auth.models import User

class HealthData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    steps = models.IntegerField()
    sleep_hours = models.FloatField()
    heart_rate = models.IntegerField()
