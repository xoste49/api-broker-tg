import asyncio

from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from server.apps.telegram.bot import TelegramBot
from server.apps.telegram.models import TelegramTokenUserModel, TOKEN_LENGTH, TelegramUserModel


class TelegramViewSet(APIView):
    """View для работы с Telegram"""

    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['get'], detail=False)
    def get(self, request):
        """Получает токен для Telegram"""
        try:
            token_user = TelegramTokenUserModel.objects.get(user=request.user)
        except TelegramTokenUserModel.DoesNotExist:
            token_user = TelegramTokenUserModel.objects.create(
                user=request.user,
                token=get_random_string(TOKEN_LENGTH),
            )
        resp = {
            'token': token_user.token
        }
        return Response(resp, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def post(self, request):
        """Отправляет сообщение в Telegram"""
        data = dict(request.data)
        text: str = str(data.get('text', ''))
        if not text:
            return Response(
                {'error': 'Не передан параметр text'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            token_user = TelegramTokenUserModel.objects.get(user=request.user)
        except TelegramTokenUserModel.DoesNotExist:
            return Response(
                {'error': 'Вы ещё не создали токена для работы с Telegram'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for tg_user in TelegramUserModel.objects.filter(token=token_user.token):
            msg = f'{request.user.username}, я получил от тебя сообщение:\n{text}'
            asyncio.run(TelegramBot.send_message(msg, tg_user.tg_id))
        return Response(status=status.HTTP_201_CREATED)
