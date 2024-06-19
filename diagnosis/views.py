from django.shortcuts import render
from .models import BodyParts,Symptom,Disease
from rest_framework import generics  # type: ignore
from .api.serializers import DiseaseSerializer
import json
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response 
from rest_framework.renderers import JSONRenderer # type: ignore
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def show_parts(request):
    if request.method == 'GET':
        parts = BodyParts.objects.all()
        context = {'form':parts}

        return render(request,'diagnosis_form.html',context)
        

def show_symptoms(request,id):
    name_instance = BodyParts.objects.get(id=id)
    part_instance = BodyParts.objects.get(name=name_instance)
    symptoms = Symptom.objects.filter(part = part_instance)
    context = {'symptoms':symptoms}
    return render(request,'symptom_page.html',context)
 
def show_disease(request,id,id_symptom):
    name_instance = Symptom.objects.get(id=id_symptom)
    part_instance = Symptom.objects.get(name=name_instance)
    disease = Disease.objects.filter(symptom = part_instance)
    context = {'disease':disease}
    return render(request,'disease_page.html',context)
        
class DiseaseListView(generics.ListAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer      

def AnalyzeSymptoms(request):
    if request.method == 'POST': 
        payload = json.loads(request.body)
        disease = Disease.objects.latest("1")
        serializer = DiseaseSerializer(disease)
        serializedData = serializer.data

        return JSONRenderer.render(serializedData)
    
class DiseaseEnrollView(APIView):
    def post(self, request, pk, format=None):
        payload = request.body
        
        response_data = {
                'message': 'Data received',
                'name': "Haile",
                'age': "34"
            }
        return Response({'enrolled':True})
