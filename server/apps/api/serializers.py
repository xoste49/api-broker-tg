from rest_framework import serializers

from server.apps.api.models import MessageModel


class MessagesSerializer(serializers.ModelSerializer):
    """Messages serializer."""

    class Meta:
        model = MessageModel
        fields = [
            'user',
            'text',
            'datatime_create',
        ]
