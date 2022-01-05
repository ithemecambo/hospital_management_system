from django.urls import path
from .admin_views import (
    CategoryView,
    add_category,
    update_category,
    delete_category,
    ManufacturerView,
    add_manufacture,
    update_manufacturer,
    delete_manufacturer,
    MedicineTypeView,
    add_medicine_type,
    update_medicine_type,
    delete_medicine_type,
    UnitView,
    add_unit,
    update_unit,
    delete_unit,
    MedicineView,
    add_medicine,
    update_medicine,
    delete_medicine,
)

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('add-category/', add_category, name='add-category'),
    path('update-category/<int:pk>', update_category, name='update-category'),
    path('delete-category/<int:pk>', delete_category, name='delete-category'),

    path('manufacturers/', ManufacturerView.as_view(), name='manufacturers'),
    path('add-manufacturer/', add_manufacture, name='add-manufacturer'),
    path('update-manufacturer/<int:pk>', update_manufacturer, name='update-manufacturer'),
    path('delete-manufacturer/<int:pk>', delete_manufacturer, name='delete-manufacturer'),

    path('medicine-types/', MedicineTypeView.as_view(), name='medicine-types'),
    path('add-medicine-type/', add_medicine_type, name='add-medicine-type'),
    path('update-medicine-type/<int:pk>', update_medicine_type, name='update-medicine-type'),
    path('delete-medicine-type/<int:pk>', delete_medicine_type, name='delete-medicine-type'),

    path('units/', UnitView.as_view(), name='units'),
    path('add-unit/', add_unit, name='add-unit'),
    path('update-unit/<int:pk>', update_unit, name='update-unit'),
    path('delete-unit/<int:pk>', delete_unit, name='delete-unit'),

    path('medicines/', MedicineView.as_view(), name='medicines'),
    path('add-medicine/', add_medicine, name='add-medicine'),
    path('update-medicine/<int:pk>', update_medicine, name='update-medicine'),
    path('delete-medicine/<int:pk>', delete_medicine, name='delete-medicine'),
]