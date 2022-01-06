from django.urls import path
from .admin_views import (
    LoginView,
    RegisterView,
    ForgotPasswordView,
    ChangePasswordSettingsView,
    LookScreenView,
    EditProfileView,
    ProfileView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('change-password/', ChangePasswordSettingsView.as_view(), name='change-password'),
    path('lock-screen/', LookScreenView.as_view(), name='lock-screen'),
    path('edit-profile/', EditProfileView.as_view(), name='edit-profile'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
