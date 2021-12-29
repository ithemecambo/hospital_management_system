from django.urls import path
from .admin_views import (
    CategoryView,
    ManufacturerView,
    MedicineTypeView,
    UnitView,
    MedicineView
)

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('manufacturers/', ManufacturerView.as_view(), name='manufacturers'),
    path('medicine-types/', MedicineTypeView.as_view(), name='medicine-types'),
    path('units/', UnitView.as_view(), name='units'),
    path('medicines/', MedicineView.as_view(), name='medicines'),
]