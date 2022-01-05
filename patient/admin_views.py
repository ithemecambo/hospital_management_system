from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView

from patient.forms import *
from patient.models import *


class BloodTypeView(ListView):
    template_name = 'admin/patient/blood-type.html'
    context_object_name = 'bloodTypes'
    queryset = BloodBank.objects.all()


def add_blood_type(request):
    form = BloodBankCreateForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Blood Saved Success')
        return redirect('../blood-types')
    context = {
        'title': 'Add Blood',
        'form': form
    }
    return render(request, 'admin/patient/add-blood-type.html', context)


def update_blood(request, pk):
    queryset = BloodBank.objects.get(id=pk)
    form = BloodBankUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = BloodBankUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blood Updated Success')
    context = {
        'title': 'Update Blood',
        'form': form
    }
    return render(request, 'admin/patient/add-blood-type.html', context)


def delete_blood(request, pk):
    queryset = BloodBank.objects.get(id=pk)
    queryset.delete()
    messages.success(request, 'Blood Deleted Success')
    return redirect('../blood-types')


class PatientView(ListView):
    template_name = 'admin/patient/patients.html'
    context_object_name = 'patients'
    queryset = Patient.objects.all()


def add_patient(request):
    form = PatientCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Patient Saved Success')
        return redirect('../patients')
    context = {
        'title': 'Add Patient',
        'form': form
    }
    return render(request, 'admin/patient/add-patient.html', context)


def update_patient(request, pk):
    queryset = Patient.objects.get(id=pk)
    form = PatientUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient Updated Success')
            return redirect('../patients')
    context = {
        'title': 'Update Patient',
        'form': form
    }
    return render(request, 'admin/patient/add-patient.html', context)


def delete_patient(request, pk):
    queryset = Patient.objects.get(id=pk)
    queryset.delete()
    messages.success(request, 'Patient Deleted Success')
    return redirect('../patients')
