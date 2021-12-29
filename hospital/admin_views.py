from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import *

from appointment.models import *
from hospital.forms import *
from medicine.models import *
from patient.models import *
from hospital.models import *


def index(request):
    context = {
        'title': 'RMS - Medical & Hospital',
        'queryset': 'Home'
    }
    return render(request, 'admin/dashboard/dashboard.html', context)


class HomeView(ListView):
    template_name = 'admin/dashboard/dashboard.html'
    queryset = Doctor.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['appointments'] = Appointment.objects.all()
        context['specialities'] = Speciality.objects.all()
        context['departments'] = Department.objects.all()
        context['medicines'] = Medicine.objects.all()
        context['patients'] = Patient.objects.all()
        context['doctors'] = Doctor.objects.all()

        return context


class DepartmentView(ListView):
    model = Department
    template_name = 'admin/department/departments.html'
    context_object_name = 'departments'
    queryset = Department.objects.all()


class AmbulanceView(ListView):
    model = Ambulance
    template_name = 'admin/ambulance/ambulances.html'
    context_object_name = 'ambulances'
    queryset = Ambulance.objects.all()
    ordering = ['-year']


class AmbulanceCreateFormView(FormView):
    form_class = AmbulanceCreateForm
    template_name = 'admin/ambulance/add-ambulance.html'
    success_url = '../ambulances'

    def form_valid(self, form):
        object = form.save(commit=False)
        form.save()
        if self.request.FILES:
            for afile in self.request.FILES.getlist('photo_url'):
                img = object.photo_url.create(picture=afile)

        return super(AmbulanceCreateFormView, self).form_valid(form)


def add_ambulance(request):
    form = AmbulanceCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Ambulance Saved Success')
        return redirect('../ambulances')
    context = {
        'title': 'Add Ambulance',
        'form': form,
    }
    return render(request, 'admin/ambulance/add-ambulance.html', context)


def update_ambulance(request, pk):
    queryset = Ambulance.objects.get(id=pk)
    form = AmbulanceUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = AmbulanceUpdateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ambulance Updated Success')
            return redirect('../ambulances')
    context = {
        'title': 'Update Ambulance',
        'form': form
    }
    return render(request, 'admin/ambulance/add-ambulance.html', context)


def delete_ambulance(request, pk):
    queryset = Ambulance.objects.get(id=pk)
    queryset.delete()
    messages.success(request, 'Ambulance Deleted Success')
    return redirect('../ambulances')


class LanguageView(ListView):
    model = Language
    template_name = 'admin/hospital/languages.html'
    context_object_name = 'languages'
    queryset = Language.objects.all()


class SpecialityView(ListView):
    model = Speciality
    template_name = 'admin/hospital/specialities.html'
    context_object_name = 'specialities'
    queryset = Speciality.objects.all()

