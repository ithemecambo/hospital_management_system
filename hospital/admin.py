from django.contrib import admin

from .forms import *
from .models import *


class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentCreateForm

    list_display = [
        'id',
        'icon',
        'title',
        'get_description',
        'status'
    ]
    list_display_links = [
        'icon',
        'title'
    ]
    list_filter = [
        'created_date',
        'status'
    ]
    search_fields = [
        'title',
        'description'
    ]
    ordering = ['id']
    list_per_page = 15


class AmbulanceAdmin(admin.ModelAdmin):
    form = AmbulanceCreateForm
    list_display = [
        'id',
        'photo',
        'vehicle_number',
        'vehicle', 'driver_name',
        'driver_contact',
        'vehicle_type',
        'driver_license',
        'status'
    ]
    list_display_links = [
        'photo',
        'vehicle_number',
        'vehicle',
        'driver_name',
        'driver_contact'
    ]
    list_filter = [
        'created_date',
        'status'
    ]
    search_fields = [
        'vehicle_number',
        'make',
        'model',
        'year',
        'driver_name',
        'driver_contact'
    ]
    ordering = ['id']
    list_per_page = 15


class SpecialityAdmin(admin.ModelAdmin):
    form = SpecialityCreateForm
    list_display = [
        'id',
        'name',
        'status'
    ]
    list_filter = [
        'created_date',
        'status'
    ]
    search_fields = [
        'name'
    ]
    ordering = ['id']
    list_per_page = 15


class LanguageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'logo',
        'name',
        'country',
        'code',
        'get_dial_code',
        'status'
    ]
    list_display_links = [
        'logo',
        'name',
        'country'
    ]
    list_filter = [
        'created_date',
        'status'
    ]
    search_fields = [
        'name',
        'country'
    ]
    ordering = ['country']
    list_per_page = 15


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0


class EducationInline(admin.StackedInline):
    model = Education
    extra = 0


class DoctorAdmin(admin.ModelAdmin):
    form = DoctorCreateForm
    list_display = [
        'id',
        'profile',
        'name',
        'gender',
        'dob',
        'nationality',
        'phone',
        'email',
        'address',
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
        'status',
    ]
    search_fields = [
        'name',
        'gender',
        'dob',
        'nationality',
        'phone',
        'email'
    ]
    ordering = ['id']
    list_per_page = 15
    inlines = [ExperienceInline, EducationInline]


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Ambulance, AmbulanceAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Doctor, DoctorAdmin)
