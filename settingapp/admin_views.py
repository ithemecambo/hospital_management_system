from django.views.generic import TemplateView


class CompanySettingsView(TemplateView):
    template_name = 'admin/settings/company-settings.html'


class LocalizationSettingsView(TemplateView):
    template_name = 'admin/settings/localization.html'


class ThemeSettingsView(TemplateView):
    template_name = 'admin/settings/theme-settings.html'


class RolePermissionSettingsView(TemplateView):
    template_name = 'admin/settings/roles-permissions.html'


class InvoiceSettingsView(TemplateView):
    template_name = 'admin/settings/invoice-settings.html'


class NotificationSettingsView(TemplateView):
    template_name = 'admin/settings/notification-settings.html'


class ChangePasswordSettingsView(TemplateView):
    template_name = 'admin/settings/change-password.html'


class StaffView(TemplateView):
    template_name = 'admin/staff/staffs.html'


class LeaveView(TemplateView):
    template_name = 'admin/staff/leaves.html'


class HolidayView(TemplateView):
    template_name = 'admin/staff/holidays.html'


class AttendanceView(TemplateView):
    template_name = 'admin/staff/attendance.html'
