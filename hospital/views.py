from django.shortcuts import render
from django.views.generic import ListView
from hospital.models import *


def index(request):
    context = {
        'title': 'Hospital Management System',
        'queryset': 'Home'
    }
    return render(request, 'admin/dashboard/index.html', context)


class HomeView(ListView):
    template_name = 'hospital/index.html'
    queryset = Doctor.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['specialities'] = Speciality.objects.all()
        context['departments'] = Department.objects.all()
        context['doctors'] = Doctor.objects.all()
        # context['slides'] = Slider.objects.all()

        return context
