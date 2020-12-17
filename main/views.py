from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Patient
from .forms import PatientForm
def home(request):
    data=Patient.objects.all()
    return render(request,'home.html',{'data':data})

# Add Patient
def addPatient(request):
    form=PatientForm
    if request.method=='POST':
        saveForm=PatientForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'Data has been added.')
    return render(request,'add-patient.html',{'form':form})

# Update Patient
def updatePatient(request,id):
    patient=Patient.objects.get(id=id)
    if request.method=='POST':
        saveForm=PatientForm(request.POST,instance=patient)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'Data has been updated.')
    form=PatientForm(instance=patient)
    return render(request,'update-patient.html',{'form':form})

# Delete
def deletePatient(request,id):
    Patient.objects.filter(id=id).delete()
    return redirect('/')

# Send Email
def sendEmail(request,id):
    patient=Patient.objects.get(id=id) 
    send_mail(
        'Next Visit Reminder',
        'Your next visit is on '+ str(patient.next_visit_date),
        'admin@example.com',
        [patient.email],
        fail_silently=False,
    )
    messages.success(request,'Mail has been sent.')
    return redirect('/')