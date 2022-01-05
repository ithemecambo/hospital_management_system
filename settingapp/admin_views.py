from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from settingapp.forms import *


class CompanySettingsView(TemplateView):
    template_name = 'admin/settings/company-settings.html'


def add_company_setting(request):
    form = CompanySettingCreateForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Company Setting Saved Success')
        return redirect('../medicine-types')
    context = {
        'title': 'Company Setting',
        'form': form
    }
    return render(request, 'admin/settings/company-settings.html', context)


def update_company_setting(request, pk):
    queryset = CompanySetting.objects.get(id=pk)
    form = CompanySettingCreateForm(instance=queryset)
    if request.method == 'POST':
        form = CompanySettingCreateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company Setting Updated Success')
            return redirect('../company-settings')
    context = {
        'title': 'Company Setting',
        'form': form
    }
    return render(request, 'admin/settings/company-settings.html', context)


class LocalizationSettingsView(TemplateView):
    template_name = 'admin/settings/localization.html'


class ThemeSettingsView(TemplateView):
    template_name = 'admin/settings/theme-settings.html'


class RolePermissionSettingsView(TemplateView):
    template_name = 'admin/settings/roles-permissions.html'


class InvoiceSettingsView(TemplateView):
    template_name = 'admin/settings/invoice-settings.html'


class NotificationSettingsView(TemplateView):
    template_name = 'admin/settings/notifications-settings.html'


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
