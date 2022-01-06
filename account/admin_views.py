from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'admin/auth/login.html'


class RegisterView(TemplateView):
    template_name = 'admin/auth/register.html'


class ForgotPasswordView(TemplateView):
    template_name = 'admin/auth/forgot-password.html'


class ChangePasswordSettingsView(TemplateView):
    template_name = 'admin/settings/change-password.html'


class LookScreenView(TemplateView):
    template_name = 'admin/auth/lock-screen.html'


class ProfileView(TemplateView):
    template_name = 'admin/auth/profile.html'


class EditProfileView(TemplateView):
    template_name = 'admin/auth/edit-profile.html'

