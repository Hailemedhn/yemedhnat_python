from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
               path('',views.index,name='index'),
               path('index.html',views.index,name='index'),
               path('about.html',views.about,name='about'),
               path('address.html',views.address,name='address'),
                path('appointment', views.appointment, name='appointment'),

]