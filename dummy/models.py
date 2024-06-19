from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name