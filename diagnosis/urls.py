from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("diagnosis_form/",views.show_parts,name='diagnosis_form'),
    path("diagnosis_form/<int:id>/",views.show_symptoms,name='symptom_page'),
    path("diagnosis_form/<int:id>/<int:id_symptom>/",views.show_disease,name='disease_page'),
    path('disease/', views.DiseaseListView.as_view(), name='disease_list'),
    path('test/', views.DiseaseEnrollView.as_view(), name='test'),
]