from django.shortcuts import render
from dummy.froms import AppointmentForm
from dummy.models import Appointment
# Create your views here.
def index(request):
    return render(request,'index.html')

def address(request):
    return render(request,'address.html')

def about(request):
    return render(request,'about.html')

def appointment(request):
    if request.method == 'POST':
        appointment = AppointmentForm(data=request.POST)
        if appointment.is_valid():
            appointment_obj = appointment.save(commit=False)
            

            appointment_obj.save()
            
            return render(request,'appointment_done.html',{'form': appointment_obj})
   
    else:
        appointment = AppointmentForm()
    return render(request,'appointment.html',{'form': appointment})
