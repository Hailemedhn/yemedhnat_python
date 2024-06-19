from django.contrib import admin
from .models import BodyParts,Symptom,Disease

# Register your models here.
admin.site.register(BodyParts)
admin.site.register(Symptom)
admin.site.register(Disease)