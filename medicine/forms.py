from django import forms
from medicine.models import *


class ManufacturerCreateForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'phone', 'address', 'balance', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name

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


class ManufacturerUpdateForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'phone', 'address', 'balance', 'status', 'description']


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'icon']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        for cat in Category.objects.all():
            if cat.name == name:
                raise forms.ValidationError(name + ' is already created')
        return name


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'icon', 'status']


class MedicineTypeCreateForm(forms.ModelForm):
    class Meta:
        model = MedicineType
        fields = ['name', 'icon']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name


class MedicineTypeUpdateForm(forms.ModelForm):
    class Meta:
        model = MedicineType
        fields = ['name', 'icon', 'status']


class UnitCreateForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name', 'icon']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name


class UnitUpdateForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name', 'icon', 'status']


class MedicineCreateForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['barcode_or_qrcode', 'medicine_name', 'strength', 'generic_name', 'box_size', 'manufacturer',
                  'category', 'medicine_type', 'unit', 'medicine_shelf', 'manufacturer_price', 'sell_price',
                  'tax', 'vat', 'photo_url', 'description']

    def clean_barcode_or_qrcode(self):
        barcode_or_qrcode = self.cleaned_data.get('barcode_or_qrcode')
        if not barcode_or_qrcode:
            raise forms.ValidationError('This field is required')
        return barcode_or_qrcode

    def clean_medicine_name(self):
        medicine_name = self.cleaned_data.get('medicine_name')
        if not medicine_name:
            raise forms.ValidationError('This field is required')
        return medicine_name

    def clean_generic_name(self):
        generic_name = self.cleaned_data.get('generic_name')
        if not generic_name:
            raise forms.ValidationError('This field is required')
        return generic_name

    def clean_manufacturer(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        if not manufacturer:
            raise forms.ValidationError('This field is required')
        return manufacturer

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')
        return category

    def clean_medicine_type(self):
        medicine_type = self.cleaned_data.get('medicine_type')
        if not medicine_type:
            raise forms.ValidationError('This field is required')
        return medicine_type

    def clean_unit(self):
        unit = self.cleaned_data.get('unit')
        if not unit:
            raise forms.ValidationError('This field is required')
        return unit

    def clean_manufacturer_price(self):
        manufacturer_price = self.cleaned_data.get('manufacturer_price')
        if not manufacturer_price:
            raise forms.ValidationError('This field is required')
        return manufacturer_price

    def clean_sell_price(self):
        sell_price = self.cleaned_data.get('sell_price')
        if not sell_price:
            raise forms.ValidationError('This field is required')
        return sell_price


class MedicineUpdateForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['barcode_or_qrcode', 'medicine_name', 'strength', 'generic_name', 'box_size', 'manufacturer',
                  'category', 'medicine_type', 'unit', 'medicine_shelf', 'manufacturer_price', 'sell_price',
                  'tax', 'vat', 'photo_url', 'status', 'description']

