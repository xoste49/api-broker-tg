from django.urls import path

from server.apps.api.views import TelegramViewSet


urlpatterns = [
    path('tg/', TelegramViewSet.as_view()),
]
