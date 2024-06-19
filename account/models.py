from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    blood_type = models.CharField(max_length=3)
    emergency_contact_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=25)
    height = models.IntegerField()
    weight = models.DecimalField(max_digits=5,decimal_places=2)
    card_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    last_appointment = models.DateField(blank=True,null=True)
    next_appointment = models.DateField(blank=True,null=True)
    phone_number = models.CharField(max_length=15,unique=True,default="00000000")
    orders=models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'