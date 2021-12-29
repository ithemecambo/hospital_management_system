from django.contrib import admin
from appointment.forms import *
from appointment.models import *


class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentCreateForm
    list_display = [
        'patient',
        'doctor',
        'date',
        'shift',
        'time',
        'status'
    ]
    list_filter = [
        'date',
        'status'
    ]
    search_fields = [
        'doctor__name',
        'patient__name',
    ]
    date_hierarchy = 'date'
    ordering = ['-date']
    list_per_page = 15


admin.site.register(Appointment, AppointmentAdmin)
