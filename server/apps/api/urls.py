from django.urls import path
from rest_framework import routers


from server.apps.api.views import TelegramViewSet, MessagesViewSet

router = routers.SimpleRouter()
router.register('msgs', MessagesViewSet, basename='messages')

urlpatterns = [
    path('tg/', TelegramViewSet.as_view()),
] + router.urls
