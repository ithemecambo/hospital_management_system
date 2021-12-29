from django.views.generic import ListView
from appointment.models import *


class AppointmentView(ListView):
    template_name = 'admin/appointment/appointments.html'
    context_object_name = 'appointments'
    queryset = Appointment.objects.all()