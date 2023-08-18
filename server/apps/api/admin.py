from django.contrib import admin

from server.apps.api.models import MessageModel


@admin.register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    """Admin panel ``MessageModel`` model."""
    list_display = ('user', 'text', 'datatime_create')

