from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView

from appointment.forms import *
from appointment.models import *


class AppointmentView(ListView):
    template_name = 'admin/appointment/appointments.html'
    context_object_name = 'appointments'
    queryset = Appointment.objects.all()


def add_appointment(request):
    form = AppointmentCreateForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Appointment Saved Success')
        return redirect('../appointments')
    context = {
        'title': 'Add Appointment',
        'form': form
    }
    return render(request, 'admin/appointment/add-appointment.html', context)


def update_appointment(request, pk):
    queryset = Appointment.objects.get(id=pk)
    form = AppointmentUpdateForm(instance=queryset)
    # if request.method == 'POST':
    #     form = AppointmentUpdateForm(request.POST, instance=queryset)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Appointment Updated Success')
    #         return redirect('../appointments')
    context = {
        'title': 'Update Appointment',
        'form': form
    }
    return render(request, 'admin/appointment/app-appointment.html', context)


def delete_appointment(request, pk):
    queryset = Appointment.objects.get(id=pk)
    queryset.delete()
    messages.success(request, 'Appointment Deleted Success')
    return redirect('../appointments')