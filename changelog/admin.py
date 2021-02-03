from django.contrib import admin
from .models import ChangeLog


@admin.register(ChangeLog)
class ChangeLogAdmin(admin.ModelAdmin):
    list_display = ('changed', 'model', 'user', 'record_id', 'data',
                    'ipaddress', 'action_on_model',)
    readonly_fields = ('user',)
    list_filter = ('model', 'action_on_model',)
