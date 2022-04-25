from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .serializers import GoodsReviewSerializer
from .models import god_god_evl;
from django.db import connection, connections
import requests
import json
from PyKomoran import Komoran, DEFAULT_MODEL
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getGoodsReview(request, god_no):
    if request.method == 'GET':
        goodsReview = god_god_evl.objects.filter(god_no=god_no)

        #페이징처리 해야됨
        serializer = GoodsReviewSerializer(goodsReview, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getGoodsTotalCnt(request, god_no):
    if request.method == 'GET':
        goodsReview = god_god_evl.objects.filter(god_no=god_no).order_by('-god_evl_turn')[0:1]
        #페이징처리 해야됨
        serializer = GoodsReviewSerializer(goodsReview, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)