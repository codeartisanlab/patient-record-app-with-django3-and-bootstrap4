from django import forms
from .models import Patient
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=('full_name','email','mobile_no','address','detail','precout','next_visit_date')