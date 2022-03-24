from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import live, live_chat
from django.db import connection, connections
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def emotionController(request):
    liveChatData = live_chat.objects.filter()
    # print(liveChatData)
    print("Hello World")
    return Response(data=liveChatData, status=status.HTTP_200_OK)

def index_home(request):
    print("Hello World")