import requests
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .serializers import LiveChatSerializer, LiveKeywordRankSerializer
from .models import live, live_chat, live_keyword_rank
from django.db import connection, connections
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import pandas as pd
from collections import Counter
import wordcloud
from PyKomoran import Komoran, DEFAULT_MODEL
import os

@api_view(['GET', 'POST'])
def keywordController(request):
    if request.method == 'GET':
        liveChatData = live_chat.objects.filter(live_id='994').values()
        # print(liveChatData)
    return Response(data=liveChatData, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def keywordPKController(request, live_id):
    liveChatData = live_chat.objects.all()
    liveChatDataId = {}
    if live_id:
        liveChatDataId = liveChatData.filter(live_id=live_id)
    serializer = LiveChatSerializer(liveChatDataId, many=True)

    content = live_chat.objects.filter(live_id=live_id).values('chat_cont')
    df = pd.DataFrame(content)

    makeWordCloud(df.chat_cont)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','POST', 'DELETE', 'PUT'])
def insertLiveChatKeywordController(request, live_id):
    liveChatDataId = live_keyword_rank.objects.filter(live_id=live_id)
    print(request.method)
    print(request)
    if request.method == 'GET':
        serializer = LiveKeywordRankSerializer(liveChatDataId, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if len(liveChatDataId) == 0:
            liveChatData = live_chat.objects.filter(live_id=live_id)
            words = []
            for chatData in liveChatData:
                words.append(chatData.chat_cont)
            
            noun_list = keywordAnalytics(words)
            print(noun_list)

            for i in range(0,len(noun_list)):                
                live_id = live_id
                keyword_rank = i+1
                keyword = noun_list[i][0]
                keyword_freq = noun_list[i][1]
                live_keyword_rank(live_id=live_id, keyword_rank=keyword_rank, keyword=keyword, keyword_freq=keyword_freq).save()
        elif len(liveChatDataId) > 0 :
            serializer = LiveKeywordRankSerializer(liveChatDataId, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
            
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def index_home(request):
    print("Hello World")

komoran = Komoran("EXP")

def keywordAnalytics(words):
    nouns=[]
    for t in words:
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

def makeWordCloud(contents):
    fontpath = 'H2GTRM.ttf'
    # filename = os.path.join('', 'images\wordcloud01.png')        

    wordcloud = wordcloud.WordCloud(font_path=fontpath, background_color='white',max_font_size=100)
    wordcloud.generate_from_frequencies(dict(contents))
    wordcloud.to_file('wordcloud01.png')