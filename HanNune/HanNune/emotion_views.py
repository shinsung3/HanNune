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

@api_view(['GET','POST', 'DELETE', 'PUT'])
def getOrPostSentiwordScore(request, live_id):
    print(request.method)
    print(request)
    liveChatDataId = sentiword_live_score.objects.filter(live_id=live_id)
    if request.method == 'GET':
        serializer = SentiWordLiveScoreSerializer(liveChatDataId, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        dic = {"-2":0, "-1":0, "0":0, "1":0, "2":0}
        if len(liveChatDataId) == 0:
            liveChatData = live_chat.objects.filter(live_id=live_id)
            for chatData in liveChatData:
                dic = emotionAnalytics(chatData.chat_cont)
            id = live_id
            power_negative = dic['-2']
            negative = dic['-1']
            neutrality = dic['0']
            positive = dic['1']
            power_positive = dic['2']
            live_id = live_id
            total = int(power_negative) + int(negative) + int(positive) + int(power_positive)
            sentiword_live_score(id=id,power_negative=power_negative, negative=negative, neutrality=neutrality, positive=positive,
                            power_positive=power_positive,live_id=live_id, total=total).save()
            # serializer = LiveChatSerializer(data=request.data, many=True)
            # print(serializer)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'DELETE', 'PUT'])
def getLiveChatSentiwordScore(request):
    liveChatData = sentiword_live_score.objects.values()
    # print(liveChatData)
    if request.method == 'GET':
        serializer = SentiWordLiveScoreSerializer(liveChatData, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

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
    # print(word)
    if "즤" not in word:
        tokens = komoran.get_morphes_by_tags(word, tag_list=['NNP', 'NNG', 'VA']) #고유 명사, 일반 명사, 형용사만 추출
        # print(len(tokens))
        # print("-2:매우 부정, -1:부정, 0:중립 or Unkwon, 1:긍정, 2:매우 긍정")
        if len(tokens)>0:
            for token in tokens:
                wordname = token.strip(" ")
                # print(wordname)
                root, score = ksl.data_list(wordname)
                score = str(score)
                dic[score] = dic[score]+1
                # print(dic)
    return dic