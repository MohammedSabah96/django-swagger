from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'is_completed',
                    'active', 'created_at', 'updated_at']
    list_display_links = ['id', 'user', 'title']
    list_editable = ['is_completed']
    list_filter = ['created_at', 'is_completed']
    readonly_fields = ['user', 'created_at', 'updated_at']
    search_fields = ['title', 'memo']
    list_per_page = 20


admin.site.register(Todo, TodoAdmin)
