from django import forms
from appointment.models import *


class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'shift', 'time', 'note']

    def clean_patient(self):
        patient = self.cleaned_data.get('patient')
        if not patient:
            raise forms.ValidationError('This field is required')
        return patient

    def clean_doctor(self):
        doctor = self.cleaned_data.get('doctor')
        if not doctor:
            raise forms.ValidationError('This field is required')
        return doctor

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if not date:
            raise forms.ValidationError('This field is required')
        return date

    def clean_shift(self):
        shift = self.cleaned_data.get('shift')
        if not shift:
            raise forms.ValidationError('This field is required')
        return shift

    def clean_time(self):
        time = self.cleaned_data.get('time')
        if not time:
            raise forms.ValidationError('This field is required')
        return time


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'shift', 'time', 'status', 'note']

