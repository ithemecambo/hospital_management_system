from django.urls import path, include
from hospital.api import views
from hospital.api.views import (
    languages,
)

app_name = 'hospital'

urlpatterns = [
    path('languages/', languages, name=None),
]