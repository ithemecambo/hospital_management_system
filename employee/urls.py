from django.urls import path
from employee import views

urlpatterns = [
    path('', views.index),
]