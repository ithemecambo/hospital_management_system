from django.urls import path
from .admin_views import (
    BloodTypeView,
    PatientView,
)

urlpatterns = [
    path('blood-types/', BloodTypeView.as_view(), name='blood-types'),
    path('patients/', PatientView.as_view(), name='patients'),
]