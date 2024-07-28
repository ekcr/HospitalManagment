from django import forms
from .models import Doctors

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['name', 'department']
