from django.shortcuts import render
from .models import Patient
def home(request):
    data=Patient.objects.all()
    return render(request,'home.html',{'data':data})
