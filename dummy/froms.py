from django import forms
from django.contrib.auth.models import User
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model  = Appointment
        fields = ('name','last_name','date','time',)