from django import forms

from settingapp.models import *


class CompanySettingCreateForm(forms.ModelForm):
    class Meta:
        model = CompanySetting
        fields = ['company_name', 'contact_person', 'address', 'country', 'city', 'state_province',
                  'postal_code', 'email', 'phone_number', 'mobile_number', 'fax', 'website_url']


class LocalizationCreateForm(forms.ModelForm):
    class Meta:
        model = Localization
        fields = ['country', 'date_format', 'timezone', 'language', 'currency_code', 'currency_symbol']


class ThemeSettingCreateForm(forms.ModelForm):
    class Meta:
        model = ThemeSetting
        fields = ['website_name', 'light_logo', 'favicon']


class InvoiceSettingCreateForm(forms.ModelForm):
    class Meta:
        model = InvoiceSetting
        fields = ['invoice_prefix', 'invoice_logo']


class SliderCreateForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title', 'caption', 'photo_url']


class NotificationCreateForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['title', 'device', 'photo_url', 'message']


