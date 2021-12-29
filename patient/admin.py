from django.contrib import admin
from patient.forms import *
from patient.models import *


class BloodBankAdmin(admin.ModelAdmin):
    form = BloodBankCreateForm
    list_display = [
        'id',
        'blood_group',
        'bag_group',
        'status'
    ]
    list_display_links = [
        'blood_group',
        'bag_group',
    ]
    search_fields = [
        'blood_group',
        'bag_group',
    ]
    list_filter = [
        'created_date',
        'status'
    ]
    ordering = ['id']
    list_per_page = 15


class PatientAdmin(admin.ModelAdmin):
    form = PatientCreateForm
    list_display = [
        'profile',
        'name',
        'gender',
        'dob',
        'phone',
        'email',
        'address',
        'doctor',
        'blood',
        'status'
    ]
    list_display_links = [
        'profile',
        'name',
        'gender',
        'dob'
    ]
    list_filter = [
        'created_date',
        'gender',
        'status'
    ]
    search_fields = [
        'name',
        'phone',
        'email',
        'address',
        'doctor__name'
    ]
    list_per_page = 15


admin.site.register(Patient, PatientAdmin)
admin.site.register(BloodBank, BloodBankAdmin)
