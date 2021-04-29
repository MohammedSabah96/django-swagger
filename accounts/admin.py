from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import UserAccount


class UserAccountAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'is_staff']
    list_filter = ['is_staff']
    fieldsets = (
        (None, {
            "fields": (
                'email', 'password'
            ),
        }),
        (_('Permissions'), {
            "fields": ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        (_('Important dates'), {"fields": ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    readonly_fields = ['last_login']
    list_per_page = 20


admin.site.register(UserAccount, UserAccountAdmin)
