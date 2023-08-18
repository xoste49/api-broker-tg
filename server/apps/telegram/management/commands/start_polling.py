from django.core.management.base import BaseCommand
from aiogram.utils import executor

from server.apps.telegram.bot import TelegramBot


class Command(BaseCommand):
    help = "Запуск телеграм бота"

    def handle(self, *args, **options):
        bot = TelegramBot()
        executor.start_polling(bot.dp)
