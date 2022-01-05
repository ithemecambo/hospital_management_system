from django.urls import path

from .admin_views import (
    HomeView,
    DepartmentView,
    add_department,
    update_department,
    delete_department,
    LanguageView,
    LanguageCreateView,
    update_language,
    delete_language,
    SpecialityView,
    add_speciality,
    update_speciality,
    delete_speciality,
    AmbulanceView,
    add_ambulance,
    update_ambulance,
    delete_ambulance,
    DoctorView,
    add_doctor,
    update_doctor,
    delete_doctor,
    DoctorScheduleView,
    add_schedule,
    update_schedule,
    delete_schedule,
)

urlpatterns = [
    path('dashboard/', HomeView.as_view(), name='dashboard'),

    path('departments/', DepartmentView.as_view(), name='departments'),
    path('add-department/', add_department, name='add-department'),
    path('update-department/<int:pk>', update_department, name='update-department'),
    path('delete-department/<int:pk>', delete_department, name='delete-department'),

    path('ambulances/', AmbulanceView.as_view(), name='ambulances'),
    path('add-ambulance/', add_ambulance, name='add-ambulance'),
    path('update-ambulance/<int:pk>', update_ambulance, name='update-ambulance'),
    path('delete-ambulance/<int:pk>', delete_ambulance, name='delete-ambulance'),

    path('doctors/', DoctorView.as_view(), name='doctors'),
    path('add-doctor/', add_doctor, name='add-doctor'),
    path('update-doctor/<int:pk>', update_doctor, name='update-doctor'),
    path('delete-doctor/<int:pk>', delete_doctor, name='delete-doctor'),

    path('doctor-schedules/', DoctorScheduleView.as_view(), name='doctor-schedules'),
    path('add-doctor-schedule/', add_schedule, name='add-doctor-schedule'),
    path('update-doctor-schedule/<int:pk>', update_schedule, name='update-doctor-schedule'),
    path('delete-doctor-schedule/<int:pk>', delete_schedule, name='delete-doctor-schedule'),

    path('languages/', LanguageView.as_view(), name='languages'),
    path('add-language/', LanguageCreateView.as_view(), name='add-language'),
    path('update-language/<int:pk>', update_language, name='update-language'),
    path('delete-language/<int:pk>', delete_language, name='delete-language'),

    path('specialities/', SpecialityView.as_view(), name='specialities'),
    path('add-speciality/', add_speciality, name='add-speciality'),
    path('update-speciality/<int:pk>', update_speciality, name='update-speciality'),
    path('delete-speciality/<int:pk>', delete_speciality, name='delete-speciality'),
]