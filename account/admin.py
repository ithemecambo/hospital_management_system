from django.contrib import admin
from account.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'profile',
        'get_full_name',
        'get_sex_display',
        'email',
        'phone',
        'fax',
        'is_admin',
        'is_staff',
        'is_active'
    ]
    list_display_links = [
        'profile',
        'get_full_name',
        'get_sex_display',
        'email',
    ]
    list_filter = [
        'created_at',
        'is_admin',
        'is_staff',
        'is_active'
    ]
    search_fields = [
        'profile',
        'get_full_name',
        'get_sex_display',
        'email',
        'phone',
    ]
    ordering = ['id']
    list_per_page = 15


admin.site.register(Account, AccountAdmin)
