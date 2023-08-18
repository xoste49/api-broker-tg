from django.contrib.auth import get_user_model
from django.db import models


class MessageModel(models.Model):
    """Сообщения"""
    user = models.ForeignKey(
        get_user_model(),
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )

    text = models.CharField(
        verbose_name='Текст сообщения',
        blank=True,
    )

    datatime_create = models.DateTimeField(
        'Дата и время сообщения',
        auto_now=True,
    )
