from django import forms
from staff.models import Staff


class StaffCreateForm(forms.ModelForm):
    model = Staff
    fields = ['staff']


class StaffUpdateForm(forms.ModelForm):
    model = Staff
    fields = ['staff']

