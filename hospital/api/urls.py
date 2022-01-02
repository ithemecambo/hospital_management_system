from django.urls import path, include
from hospital.api import views

app_name = 'hospital'

urlpatterns = [
    path('languages/', views.language_list, name=None),
]