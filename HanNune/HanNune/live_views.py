from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .serializers import LiveSerializer
from .models import live
from django.db import connection, connections
import requests
import json
from PyKomoran import Komoran, DEFAULT_MODEL
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'DELETE', 'PUT'])

def liveIdDataController(request, live_id):
    liveData = live.objects.filter(live_id=live_id)
    serializer = LiveSerializer(liveData, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def liveDataController(request):
    liveData = live.objects.values()
    serializer = LiveSerializer(liveData, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
