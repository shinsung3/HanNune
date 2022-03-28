from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .serializers import LiveChatSerializer, SentiWordInfoSerializer, SentiWordLiveScoreSerializer
from .models import live, live_chat, sentiword_info, sentiword_live_score
from django.db import connection, connections
import requests
import json
from PyKomoran import Komoran, DEFAULT_MODEL
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def emotionController(request):
    if request.method == 'GET':
        liveChatData = live_chat.objects.values()
        # print(liveChatData)
    return Response(data=liveChatData, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def emotionPKController(request, live_id):
    liveChatData = live_chat.objects.all()
    liveChatDataId = {}
    if live_id:
        liveChatDataId = liveChatData.filter(live_id=live_id)
        for chatData in liveChatDataId:
            emotionAnalytics(chatData.chat_cont)
    serializer = LiveChatSerializer(liveChatDataId, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def sentiwordController(request, searchWord):
    sentiwordInfo = sentiword_info.objects.all()
    wordInfo = {}
    if searchWord:
        wordInfo = sentiwordInfo.filter(word=searchWord)
    serializer = SentiWordInfoSerializer(wordInfo, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def updateLiveChatSentiwordController(request, live_id):
    # if live_id == None:
    #     return
    liveChatDataId = sentiword_live_score.objects.filter(live_id=live_id)
    if len(liveChatDataId) == 0:
        liveChatData = live_chat.objects.filter(live_id=live_id)
        # print(liveChatData)
        for chatData in liveChatData:
            dic = emotionAnalytics(chatData.chat_cont)
    serializer = LiveChatSerializer(liveChatDataId, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

def index_home(request):
    print("Hello World")

class KnuSL():
    def data_list(wordname):
        searchWord = sentiword_info.objects.filter(word=wordname)
        result = ['None', '0']
        if len(searchWord) != 0:
            result.pop()
            result.pop()
            result.append(searchWord[0].word_root)
            result.append(searchWord[0].polarity)
        else:
            searchWord = sentiword_info.objects.filter(word_root=wordname)
            if len(searchWord) != 0:
                result.pop()
                result.pop()
                result.append(searchWord[0].word_root)
                result.append(searchWord[0].polarity)
        root = result[0]
        score = result[1]

        return root, score

komoran = Komoran("EXP")
ksl = KnuSL
dic = {"-2":0, "-1":0, "0":0, "1":0, "2":0}
def emotionAnalytics(word):
    tokens = komoran.get_nouns(word)
    # print("-2:매우 부정, -1:부정, 0:중립 or Unkwon, 1:긍정, 2:매우 긍정")
    for token in tokens:
        wordname = token.strip(" ")
        root, score = ksl.data_list(wordname)
        score = str(score)
        dic[score] = dic[score]+1
        # print(dic)
    return dic