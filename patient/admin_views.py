from django.views.generic import ListView
from patient.models import *


class BloodTypeView(ListView):
    template_name = 'admin/patient/blood-type.html'
    context_object_name = 'bloodTypes'
    queryset = BloodBank.objects.all()


class PatientView(ListView):
    template_name = 'admin/patient/patients.html'
    context_object_name = 'patients'
    queryset = Patient.objects.all()

