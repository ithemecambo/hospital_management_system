from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView

from medicine.forms import *
from medicine.models import *


class CategoryView(ListView):
    template_name = 'admin/medicine/categories.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()


def add_category(request):
    form = CategoryCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Category Saved Success')
        return redirect('../categories')
    context = {
        'title': 'Add Category',
        'form': form
    }
    return render(request, 'admin/medicine/add-category.html', context)


def update_category(request, pk):
    queryset = Category.objects.get(id=pk)
    form = CategoryUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = CategoryUpdateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Updated Success')
            return redirect('../categories')
    context = {
        'title': 'Update Category',
        'form': form
    }
    return render(request, 'admin/medicine/add-category.html', context)


def delete_category(request, pk):
    queryset = Category.objects.get(id=pk)
    queryset.delete()
    messages.success(request, 'Category Deleted Success')
    return redirect('../categories')


class ManufacturerView(ListView):
    template_name = 'admin/medicine/manufacturers.html'
    context_object_name = 'manufacturers'
    queryset = Manufacturer.objects.all()


def add_manufacture(request):
    form = ManufacturerCreateForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Manufacturer Saved Success')
        return redirect('../manufacturers')
    context = {
        'title': 'Add Manufacturer',
        'form': form
    }
    return render(request, 'admin/medicine/add-manufacturer.html', context)


def update_manufacturer(request, pk):
    queryset = Manufacturer.objects.get(id=pk)
    form = ManufacturerUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = ManufacturerCreateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manufacturer Updated Success')
            return redirect('../manufacturers')
    context = {
        'title': 'Update Manufacturer',
        'form': form
    }
    return render(request, 'admin/medicine/add-manufacturer.html', context)


def delete_manufacturer(request, pk):
    queryset = Manufacturer.objects.get(id=pk)
    queryset.delete()
    messages.success(request, 'Manufacturer Deleted Success')
    return redirect('../manufacturers')


class MedicineTypeView(ListView):
    template_name = 'admin/medicine/medicine-type.html'
    context_object_name = 'medicineTypes'
    queryset = MedicineType.objects.all()


def add_medicine_type(request):
    form = MedicineTypeCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Medicine Type Saved Success')
        return redirect('../medicine-types')
    context = {
        'title': 'Add Medicine Type',
        'form': form
    }
    return render(request, 'admin/medicine/add-medicine-type.html', context)


def update_medicine_type(request, pk):
    queryset = MedicineType.objects.get(id=pk)
    form = MedicineTypeUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = MedicineTypeUpdateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicine Type Updated Success')
            return redirect('../medicine-types')
    context = {
        'title': 'Update Medicine Type',
        'form': form
    }
    return render(request, 'admin/medicine/add-medicine-type.html', context)


def delete_medicine_type(request, pk):
    queryset = MedicineType.objects.get(id=pk)
    queryset.delete()
    messages.success(request, 'Medicine Type Deleted Success')
    return redirect('../medicine-types')


class UnitView(ListView):
    template_name = 'admin/medicine/units.html'
    context_object_name = 'units'
    queryset = Unit.objects.all()


def add_unit(request):
    form = UnitCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Unit Saved Success')
        return redirect('../units')
    context = {
        'title': 'Add Unit',
        'form': form
    }
    return render(request, 'admin/medicine/add-unit.html', context)


def update_unit(request, pk):
    queryset = Unit.objects.get(id=pk)
    form = UnitUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = UnitUpdateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Unit Updated Success')
            return redirect('../units')
    context = {
        'title': 'Update Unit',
        'form': form
    }
    return render(request, 'admin/medicine/add-unit.html', context)


def delete_unit(request, pk):
    queryset = Unit.objects.get(id=pk)
    queryset.delete()
    messages.success(request, 'Unit Deleted Success')
    return redirect('../units')


class MedicineView(ListView):
    template_name = 'admin/medicine/medicines.html'
    context_object_name = 'medicines'
    queryset = Medicine.objects.all()


def add_medicine(request):
    form = MedicineCreateForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Medicine Saved Success')
        return redirect('../medicines')
    context = {
        'title': 'Add Medicine',
        'form': form
    }
    return render(request, 'admin/medicine/add-medicine.html', context)


def update_medicine(request, pk):
    queryset = Medicine.objects.get(id=pk)
    form = MedicineUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = MedicineUpdateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicine Updated Success')
            return redirect('../medicines')
    context = {
        'title': 'Update Medicine',
        'form': form
    }
    return render(request, 'admin/medicine/add-medicine.html', context)


def delete_medicine(request, pk):
    queryset = Medicine.objects.get(id=pk)
    queryset.delete()
    messages.success(request, 'Medicine Deleted Success')
    return redirect('../medicines')
