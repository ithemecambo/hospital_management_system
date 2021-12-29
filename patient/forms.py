from django import forms
from patient.models import *


class BloodBankCreateForm(forms.ModelForm):
    class Meta:
        model = BloodBank
        fields = ['blood', 'bag']

    def clean_blood(self):
        blood = self.cleaned_data.get('blood')
        if not blood:
            raise forms.ValidationError('This field is required')
        return blood


class BloodBankUpdateForm(forms.ModelForm):
    class Meta:
        model = BloodBank
        fields = ['blood', 'bag', 'status']


class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'gender', 'dob', 'phone', 'email', 'address', 'marital_status',
                  'doctor', 'blood', 'photo_url', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError('This field is required')
        return gender

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if not dob:
            raise forms.ValidationError('This field is required')
        return dob

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError('This field is required')
        return phone

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise forms.ValidationError('This field is required')
        return address

    def clean_marital_status(self):
        marital_status = self.cleaned_data.get('marital_status')
        if not marital_status:
            raise forms.ValidationError('This field is required')
        return marital_status


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'gender', 'dob', 'phone', 'email', 'address', 'marital_status',
                  'doctor', 'blood', 'photo_url', 'status', 'description']