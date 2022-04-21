from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .serializers import GoodsSerializer
from .models import god;
from django.db import connection, connections
import requests
import json
from PyKomoran import Komoran, DEFAULT_MODEL
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def goodsContoller(request):
    if request.method == 'GET':
        goods = god.objects.values()

        #페이징처리
        goods = goods[:10]
        serializer = GoodsSerializer(goods, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

