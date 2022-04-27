import requests
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .serializers import LiveChatSerializer, LiveKeywordRankSerializer, GoodsKeywordRankSerializer
from .models import keyword_goods_rank, live, live_chat, keyword_live_rank, god_god_evl
from django.db import connection, connections
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import pandas as pd
from collections import Counter
from PyKomoran import Komoran, DEFAULT_MODEL
import os

@api_view(['GET','POST', 'DELETE', 'PUT'])
def getOrPostKeywordRank(request, id, key):
    if key == 'live':
        liveChatDataId = keyword_live_rank.objects.filter(live_id=id)
        if request.method == 'GET':
            serializer = LiveKeywordRankSerializer(liveChatDataId, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            if len(liveChatDataId) == 0:
                liveChatData = live_chat.objects.filter(live_id=id)
                words = []
                for chatData in liveChatData:
                    words.append(chatData.chat_cont)

                noun_list = keywordAnalytics(words)

                for i in range(0,len(noun_list)):                
                    live_id = id
                    keyword_rank = i+1
                    keyword = noun_list[i][0]
                    keyword_freq = noun_list[i][1]
                    keyword_live_rank(live_id=live_id, keyword_rank=keyword_rank, keyword=keyword, keyword_freq=keyword_freq).save()
                
                return Response(status=status.HTTP_200_OK)   
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)       
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif key == "goods":
        goodsReviewDataId = keyword_goods_rank.objects.filter(god_no=id)
        if request.method == 'GET':
            serializer = GoodsKeywordRankSerializer(goodsReviewDataId, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            if len(goodsReviewDataId) == 0:
                goodsReviewData = god_god_evl.objects.filter(god_no=id)
                words = []

                for reviewData in goodsReviewData:
                    words.append(reviewData.god_evl_cont)

                noun_list = keywordAnalytics(words)

                print(noun_list)

                for i in range(0,len(noun_list)):                
                    god_no = id
                    keyword_rank = i+1
                    keyword = noun_list[i][0]
                    keyword_freq = noun_list[i][1]
                    keyword_goods_rank(god_no=god_no, keyword_rank=keyword_rank, keyword=keyword, keyword_freq=keyword_freq).save()
                
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



def index_home(request):
    print("Hello World")

komoran = Komoran("EXP")

def keywordAnalytics(words):
    nouns=[]

    for t in words:
        if '즤' not in t:
            nouns += komoran.get_morphes_by_tags(str(t), tag_list=['NNP', 'NNG', 'VA']) #고유 명사, 일반 명사, 형용사만 추출
        

    #불용어
    stop_words = "!!! !! 당 상 듀 시네 시구 해주 신주 같 스 크 레 우 앙 링 리 오 슈 다 안 작 오 이용 용 드 아아 오오 녀"
    stop_words=stop_words.split(' ')

    word_result = []
    for w in nouns:
        if w not in stop_words:
            word_result.append(w)

    word_count = Counter(word_result)
    noun_list = word_count.most_common(100)

    return noun_list