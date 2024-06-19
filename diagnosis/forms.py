from .models import Symptom,BodyParts,Disease
from django import forms

class PatientDiagnosisForm(forms.ModelForm):
    class Meta:
        model= BodyParts
        fields=('name',)