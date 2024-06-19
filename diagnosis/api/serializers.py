from rest_framework import serializers # type: ignore
from ..models import Disease

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['name',]