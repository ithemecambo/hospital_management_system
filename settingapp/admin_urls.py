from django.urls import path
from .admin_views import (
    CompanySettingsView,
    add_company_setting,
    update_company_setting,
    LocalizationSettingsView,
    ThemeSettingsView,
    RolePermissionSettingsView,
    InvoiceSettingsView,
    NotificationSettingsView,
    ChangePasswordSettingsView,

    StaffView,
    LeaveView,
    HolidayView,
    AttendanceView,
)

urlpatterns = [
    path('company-settings/', CompanySettingsView.as_view(), name='company-settings'),
    path('add-company-settings/', add_company_setting, name='add-company-settings'),
    path('update-company-settings/<int:pk>', update_company_setting, name='update-company-settings'),
    path('localization-settings/', LocalizationSettingsView.as_view(), name='localization-settings'),
    path('theme-settings/', ThemeSettingsView.as_view(), name='theme-settings'),
    path('roles-permission-settings/', RolePermissionSettingsView.as_view(), name='roles-permission-settings'),
    path('invoice-settings/', InvoiceSettingsView.as_view(), name='invoice-settings'),
    path('notification-settings/', NotificationSettingsView.as_view(), name='notification-settings'),
    path('change-password-settings/', ChangePasswordSettingsView.as_view(), name='change-password-settings'),
    path('staffs/', StaffView.as_view(), name='staffs'),
    path('leaves/', LeaveView.as_view(), name='leaves'),
    path('holidays/', HolidayView.as_view(), name='holidays'),
    path('attendances/', AttendanceView.as_view(), name='attendances'),
]
