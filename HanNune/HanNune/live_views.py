from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .serializers import LiveSerializer, LiveChatSerializer
from .models import live,live_chat
from django.db import connection, connections
import requests
import json
from PyKomoran import Komoran, DEFAULT_MODEL
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getLiveIdInfo(request, live_id):
    liveData = live.objects.filter(live_id=live_id)
    serializer = LiveSerializer(liveData, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getLiveInfo(request):
    liveData = live.objects.values()
    serializer = LiveSerializer(liveData, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getLiveChat(request):
    if request.method == 'GET':
        liveChatData = live_chat.objects.values()
        # print(liveChatData)
    return Response(data=liveChatData, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getLiveIdChat(request, live_id):
    liveChatData = live_chat.objects.all()
    liveChatDataId = {}
    if live_id:
        liveChatDataId = liveChatData.filter(live_id=live_id)
    serializer = LiveChatSerializer(liveChatDataId, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

