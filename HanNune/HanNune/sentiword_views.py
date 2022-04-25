from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .serializers import SentiWordInfoSerializer
from .models import sentiword_info
from django.db import connection, connections
import requests
import json
from PyKomoran import Komoran, DEFAULT_MODEL
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getSentiword(request, searchWord):
    sentiwordInfo = sentiword_info.objects.all()
    wordInfo = {}
    if searchWord:
        wordInfo = sentiwordInfo.filter(word=searchWord)
    serializer = SentiWordInfoSerializer(wordInfo, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)