from django import forms
from .models import *


class DepartmentCreateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title', 'logo', 'description']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('This field is required')
        for dep in Department.objects.all():
            if dep.title == title:
                raise forms.ValidationError(title + ' is already created')
        return title


class DepartmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title', 'logo', 'status', 'description']


class AmbulanceCreateForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = ['vehicle_number', 'make', 'model', 'year', 'driver_name', 'driver_contact',
                  'vehicle_type', 'driver_license', 'photo_url']


class AmbulanceUpdateForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = ['vehicle_number', 'make', 'model', 'year', 'driver_name', 'driver_contact',
                  'vehicle_type', 'driver_license', 'photo_url', 'status']


class SpecialityCreateForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ['name']


class SpecialityUpdateForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ['name', 'status']


class LanguageCreateForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'country', 'code', 'dial_code', 'flag']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name

    def clean_country(self):
        country = self.cleaned_data.get('country')
        if not country:
            raise forms.ValidationError('This field is required')
        return country

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if not code:
            raise forms.ValidationError('This field is required')
        return code

    def clean_dial_code(self):
        dial_code = self.cleaned_data.get('dial_code')
        if not dial_code:
            raise forms.ValidationError('This field is required')
        return dial_code


class LanguageUpdateForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'country', 'code', 'dial_code', 'flag', 'status']


class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'gender', 'dob', 'nationality', 'phone', 'email', 'address', 'speciality',
                  'language', 'department', 'photo_url', 'twitter', 'facebook', 'instagram', 'bio']


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'gender', 'dob', 'nationality', 'phone', 'email', 'address', 'speciality',
                  'language', 'department', 'photo_url', 'twitter', 'facebook', 'instagram', 'bio', 'status']


class DoctorScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['doctor', 'available_days', 'start_time', 'end_time', 'description']


class DoctorScheduleUpdateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['doctor', 'available_days', 'start_time', 'end_time', 'status', 'description']
