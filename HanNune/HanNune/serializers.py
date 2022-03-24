from rest_framework import serializers
from .models import live_chat

class LiveChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = live_chat
        fields = '__all__'