from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Events(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)  
    category = models.CharField(max_length=50, null=True, blank=True)  
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)  # Fixed default time to current time

    def __str__(self):
        return f"{self.name} - {self.date} {self.time.strftime('%H:%M')}"

