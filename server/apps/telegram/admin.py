from django.contrib import admin

from server.apps.telegram.models import TelegramUserModel, TelegramTokenUserModel


@admin.register(TelegramUserModel)
class TelegramUserAdmin(admin.ModelAdmin):
    """Admin panel ``TelegramUserModel`` model."""
    list_display = ('tg_id', 'first_name', 'last_name', 'username', 'is_bot', 'language_code')


@admin.register(TelegramTokenUserModel)
class TelegramTokenUserAdmin(admin.ModelAdmin):
    """Admin panel ``TelegramTokenUserModel`` model."""
    list_display = ('user', 'token')
