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
