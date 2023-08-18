from django.contrib.auth import get_user_model
from django.db import models
from django.utils.crypto import get_random_string

TOKEN_LENGTH = 50


class TelegramUserModel(models.Model):
    """Пользователь Телеграм-бота."""

    tg_id = models.BigIntegerField(
        verbose_name='Telegram user ID',
        primary_key=True,
        unique=True,
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=255,
        blank=True,
    )

    last_name = models.CharField(  # noqa: DJ01
        verbose_name='Фамилия',
        blank=True,
        null=True,
        max_length=255,
    )

    username = models.CharField(  # noqa: DJ01
        verbose_name='Username',
        blank=True,
        null=True,
        max_length=255,
    )

    is_bot = models.BooleanField(
        verbose_name='BOT',
        default=False,
    )

    language_code = models.CharField(  # noqa: DJ01
        verbose_name='Language Code',
        blank=True,
        null=True,
        max_length=10,
    )

    token = models.CharField(
        verbose_name='Токен',
        max_length=TOKEN_LENGTH,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Tg Notification Bot User'
        verbose_name_plural = 'Tg Notification Bot Users'

    def __str__(self) -> str:
        """Model string representation."""
        return f'{self.tg_id}'


class TelegramTokenUserModel(models.Model):
    """Токены пользователей"""
    user = models.OneToOneField(
        get_user_model(),
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # get_random_string(TOKEN_LENGTH)
    token = models.CharField(
        verbose_name='Токен',
        max_length=TOKEN_LENGTH,
    )

    class Meta:
        verbose_name = 'Токен для бота'
        verbose_name_plural = 'Токены для бота'

    def __str__(self) -> str:
        """Model string representation."""
        return f'{self.user} {self.token}'
