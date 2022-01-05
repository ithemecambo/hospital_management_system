from django.urls import path
from .admin_views import (
    AppointmentView,
    add_appointment,
    update_appointment,
    delete_appointment,
)

urlpatterns = [
    path('appointments/', AppointmentView.as_view(), name='appointments'),
    path('add-appointment/', add_appointment, name='add-appointment'),
    path('update-appointment/<int:pk>', update_appointment, name='update-appointment'),
    path('delete-appointment/<int:pk>', delete_appointment, name='delete-appointment'),
]