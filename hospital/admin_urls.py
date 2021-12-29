from django.urls import path

from .admin_views import (
    HomeView,
    DepartmentView,
    LanguageView,
    SpecialityView,
    AmbulanceView,
    AmbulanceCreateFormView,
    add_ambulance,
    update_ambulance,
    delete_ambulance,
)

urlpatterns = [
    path('dashboard/', HomeView.as_view(), name='dashboard'),
    path('departments/', DepartmentView.as_view(), name='departments'),
    path('languages/', LanguageView.as_view(), name='languages'),
    path('specialities/', SpecialityView.as_view(), name='specialities'),
    path('ambulances/', AmbulanceView.as_view(), name='ambulances'),
    path('add-ambulance/', add_ambulance, name='add-ambulance'),
    path('update-ambulance/<int:pk>', update_ambulance, name='update-ambulance'),
    path('delete-ambulance/<int:pk>', delete_ambulance, name='delete-ambulance'),
]