from aiogram import Bot, Dispatcher, types
from asgiref.sync import sync_to_async

from server.apps.telegram.models import TelegramUserModel
from server.settings.components import config

API_TOKEN = config('TELEGRAM_BOT_TOKEN')


class TelegramBot:
    # Initialize bot and dispatcher
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)

    @staticmethod
    @dp.message_handler(commands=['start'])
    async def start(msg: types.Message):
        try:
            tg_user = await TelegramUserModel.objects.aget(tg_id=msg.from_user.id)
        except TelegramUserModel.DoesNotExist:
            tg_user = await TelegramUserModel.objects.acreate(tg_id=msg.from_user.id)
        tg_user.first_name = msg.from_user.first_name
        tg_user.last_name = msg.from_user.last_name
        tg_user.username = msg.from_user.username
        tg_user.is_bot = msg.from_user.is_bot
        tg_user.language_code = msg.from_user.language_code
        await sync_to_async(tg_user.save)()
        await TelegramBot.bot.send_message(
            msg.from_user.id,
            'Для работы с ботом установите токен который получили '
            'от api с помощью команды "/set_token тут_ваш_токен"',
        )

    @staticmethod
    @dp.message_handler(commands=['set_token'])
    async def set_token(msg: types.Message):
        try:
            tg_user = await TelegramUserModel.objects.aget(tg_id=msg.from_user.id)
        except TelegramUserModel.DoesNotExist:
            tg_user = await TelegramUserModel.objects.acreate(tg_id=msg.from_user.id)
        token = msg.text.replace('/set_token', '').replace(' ', '')
        if token:
            # Если токен есть, то закрепляем за пользователем
            tg_user.token = token
            await sync_to_async(tg_user.save)()
            await TelegramBot.bot.send_message(
                msg.from_user.id,
                'Ваш токен сохранен',
            )
        else:
            await TelegramBot.bot.send_message(
                msg.from_user.id,
                'Токен не найден',
            )

    @staticmethod
    async def send_message(message: str, tg_id: int):
        await TelegramBot.bot.send_message(tg_id, message)
