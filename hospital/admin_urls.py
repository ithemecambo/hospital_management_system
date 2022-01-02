from django.urls import path

from .admin_views import (
    HomeView,
    DepartmentView,
    LanguageView,
    LanguageCreateView,
    update_language,
    delete_language,
    SpecialityView,
    AmbulanceView,
    AmbulanceCreateFormView,
    add_ambulance,
    update_ambulance,
    delete_ambulance,
    DoctorView,
    DoctorScheduleView
)

urlpatterns = [
    path('dashboard/', HomeView.as_view(), name='dashboard'),
    path('departments/', DepartmentView.as_view(), name='departments'),
    path('languages/', LanguageView.as_view(), name='languages'),
    path('add-language/', LanguageCreateView.as_view(), name='add-language'),
    path('update-language/<int:pk>', update_language, name='update-language'),
    path('delete-language/<int:pk>', delete_language, name='delete-language'),
    path('specialities/', SpecialityView.as_view(), name='specialities'),
    path('ambulances/', AmbulanceView.as_view(), name='ambulances'),
    path('add-ambulance/', add_ambulance, name='add-ambulance'),
    path('update-ambulance/<int:pk>', update_ambulance, name='update-ambulance'),
    path('delete-ambulance/<int:pk>', delete_ambulance, name='delete-ambulance'),
    path('doctors/', DoctorView.as_view(), name='doctors'),
    path('doctor-schedules/', DoctorScheduleView.as_view(), name='doctor-schedules'),
]