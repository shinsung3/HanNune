from rest_framework import serializers
from .models import live_chat,sentiword_info, sentiword_live_score, live_keyword_rank

class LiveChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = live_chat
        fields = '__all__'

class SentiWordInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = sentiword_info
        fields = '__all__'

class SentiWordLiveScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = sentiword_live_score
        fields = '__all__'

class LiveKeywordRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = live_keyword_rank
        fields = '__all__'