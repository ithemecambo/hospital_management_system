from django.contrib import admin
from medicine.forms import *
from medicine.models import *


class ManufacturerAdmin(admin.ModelAdmin):
    form = ManufacturerCreateForm
    list_display = ['id', 'name', 'phone', 'address', 'balance', 'status']
    list_display_links = ['name', 'phone']
    list_filter = ['created_date', 'status']
    search_fields = ['name', 'phone', 'address', 'description', 'balance']
    ordering = ['id']
    list_per_page = 15


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryCreateForm
    list_display = ['id', 'logo', 'name', 'status']
    list_display_links = ['logo', 'name']
    list_filter = ['created_date', 'status']
    search_fields = ['name']
    ordering = ['id']
    list_per_page = 15


class UnitAdmin(admin.ModelAdmin):
    form = UnitCreateForm
    list_display = ['id', 'logo', 'name', 'status']
    list_display_links = ['logo', 'name']
    list_filter = ['created_date', 'status']
    search_fields = ['name']
    ordering = ['id']
    list_per_page = 15


class MedicineTypeAdmin(admin.ModelAdmin):
    form = MedicineTypeCreateForm
    list_display = ['id', 'logo', 'name', 'status']
    list_display_links = ['logo', 'name']
    list_filter = ['created_date', 'status']
    search_fields = ['name']
    ordering = ['id']
    list_per_page = 15


class MedicineAdmin(admin.ModelAdmin):
    form = MedicineCreateForm
    list_display = [
        'id',
        'profile',
        '__str__',
        'manufacturer',
        'category',
        'medicine_type',
        'strength',
        'generic_name',
        'stock_price',
        'sell_out_price',
        'status'
    ]
    list_display_links = [
        'profile',
        '__str__',
        'medicine_type',
        'manufacturer',
        'category',
    ]
    list_filter = [
        'created_date',
        'status'
    ]
    search_fields = [
        'medicine_name',
        'strength',
        'generic_name',
        'manufacturer__name',
        'category__name',
        'medicine_type__name',
        'manufacturer_price',
        'sell_price'
    ]
    ordering = ['-created_date']
    list_per_page = 15


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(MedicineType, MedicineTypeAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Unit, UnitAdmin)
