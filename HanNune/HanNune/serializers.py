from rest_framework import serializers
from .models import god_god_evl, goods_emotion, live_chat,sentiword_info, sentiword_live_score, live_keyword_rank, live, god, sentiword_goods_score
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

class SentiWordGoodsScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = sentiword_goods_score
        fields = '__all__'

class LiveKeywordRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = live_keyword_rank
        fields = '__all__'

class LiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = live
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = god
        fields = '__all__'

class GoodsReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = god_god_evl
        fields = '__all__'

# class GoodsBestReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = sentiword_goods_score
#         fields = ('god_no','god_nm', 'evl5_cnt', 'evl4_cnt','evl3_cnt', 'evl2_cnt', 'evl1_cnt')

class GoodsEmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = goods_emotion
        fields = '__all__'