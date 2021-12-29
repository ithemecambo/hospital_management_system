from django.urls import path
from .admin_views import (
    AppointmentView,
)

urlpatterns = [
    path('appointments/', AppointmentView.as_view(), name='appointments'),
]