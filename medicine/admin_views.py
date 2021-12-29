from django.views.generic import ListView
from medicine.models import *


class CategoryView(ListView):
    template_name = 'admin/medicine/categories.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()


class ManufacturerView(ListView):
    template_name = 'admin/medicine/manufacturers.html'
    context_object_name = 'manufacturers'
    queryset = Manufacturer.objects.all()


class MedicineTypeView(ListView):
    template_name = 'admin/medicine/medicine-type.html'
    context_object_name = 'medicineTypes'
    queryset = MedicineType.objects.all()

class UnitView(ListView):
    template_name = 'admin/medicine/units.html'
    context_object_name = 'units'
    queryset = Unit.objects.all()


class MedicineView(ListView):
    template_name = 'admin/medicine/medicines.html'
    context_object_name = 'medicines'
    queryset = Medicine.objects.all()

