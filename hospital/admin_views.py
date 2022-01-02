from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
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


class DoctorView(ListView):
    template_name = 'admin/doctor/doctors.html'
    context_object_name = 'doctors'
    queryset = Doctor.objects.all()


class DoctorScheduleView(ListView):
    template_name = 'admin/hospital/doctor-schedule.html'
    context_object_name = 'schedules'
    queryset = Schedule.objects.all()


class LanguageView(ListView):
    model = Language
    template_name = 'admin/hospital/languages.html'
    context_object_name = 'languages'
    queryset = Language.objects.all()


class LanguageCreateView(FormView):
    form_class = LanguageCreateForm
    template_name = 'admin/hospital/add-language.html'
    success_url = '../languages'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        form.instance.sender = self.request.user
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Language Saved Success')
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})


class LanguageUpdateView(UpdateView):
    model = Language
    fields = ['name', 'country', 'code', 'dial_code', 'flag', 'status']
    success_url = '../languages'


def update_language(request, pk):
    queryset = Language.objects.get(id=pk)
    form = LanguageUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = LanguageUpdateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Language Updated Success')
            return redirect('../languages')
    context = {
        'form': form
    }
    return render(request, 'admin/hospital/add-language.html', context)


def delete_language(request, pk):
    queryset = Language.objects.get(id=pk)
    queryset.delete()
    messages.success(request, 'Language Deleted Success')
    return redirect('../languages')


class SpecialityView(ListView):
    model = Speciality
    template_name = 'admin/hospital/specialities.html'
    context_object_name = 'specialities'
    queryset = Speciality.objects.all()

