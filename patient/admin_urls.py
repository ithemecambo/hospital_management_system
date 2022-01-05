from django.urls import path
from .admin_views import (
    BloodTypeView,
    add_blood_type,
    update_blood,
    delete_blood,
    PatientView,
    add_patient,
    update_patient,
    delete_patient,
)

urlpatterns = [
    path('blood-types/', BloodTypeView.as_view(), name='blood-types'),
    path('add-blood-type/', add_blood_type, name='add-blood-type'),
    path('update-blood-type/<int:pk>', update_blood, name='update-blood-type'),
    path('delete-blood-type/<int:pk>', delete_blood, name='delete-blood-type'),

    path('patients/', PatientView.as_view(), name='patients'),
    path('add-patient/', add_patient, name='add-patient'),
    path('update-patient/<int:pk>', update_patient, name='update-patient'),
    path('delete-patient/<int:pk>', delete_patient, name='delete-patient'),
]