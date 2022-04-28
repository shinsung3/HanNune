from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .serializers import SentiWordLiveScoreSerializer, SentiWordGoodsScoreSerializer, GoodsEmotionSerializer
from .models import live_chat, sentiword_info, sentiword_live_score, sentiword_goods_score, god_god_evl, god, god_img
from django.db import connection, connections
import requests
import json
from PyKomoran import Komoran, DEFAULT_MODEL
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST', 'DELETE', 'PUT'])
def getOrPostSentiwordScore(request, id, key):
    print(request.method)
    if key == "live":
        liveChatDataId = sentiword_live_score.objects.filter(live_id=id)
        if request.method == 'GET':
            serializer = SentiWordLiveScoreSerializer(liveChatDataId, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            dic = {"-2":0, "-1":0, "0":0, "1":0, "2":0}
            if len(liveChatDataId) == 0:
                liveChatData = live_chat.objects.filter(live_id=id)
                for chatData in liveChatData:
                    dic = emotionAnalytics(chatData.chat_cont)
                id = id
                power_negative = dic['-2']
                negative = dic['-1']
                neutrality = dic['0']
                positive = dic['1']
                power_positive = dic['2']
                live_id = id
                total = int(power_negative) + int(negative) + int(positive) + int(power_positive)
                sentiword_live_score(id=id,power_negative=power_negative, negative=negative, neutrality=neutrality, positive=positive,
                                power_positive=power_positive,live_id=live_id, total=total).save()
                # serializer = LiveChatSerializer(data=request.data, many=True)
                # print(serializer)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    elif key == "goods":
        goodsReviewDataId = sentiword_goods_score.objects.filter(god_no=id)
        if request.method == 'GET':
            serializer = SentiWordGoodsScoreSerializer(goodsReviewDataId, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            dic = {"-2":0, "-1":0, "0":0, "1":0, "2":0}
            reviewEvl = {"5":0, "4":0, "3":0, "2":0, "1":0}
            if len(goodsReviewDataId) == 0:
                goodsReview = god_god_evl.objects.filter(god_no=id)
                goods = god.objects.filter(god_no=id)
                for review in goodsReview:
                    dic = emotionAnalytics(review.god_evl_cont)
                    if review.tot_evl_score != "None":
                        reviewEvl[review.tot_evl_score] += 1
                power_negative = dic['-2']
                negative = dic['-1']
                neutrality = dic['0']
                positive = dic['1']
                power_positive = dic['2']
                god_no = id
                total = int(power_negative) + int(negative) + int(positive) + int(power_positive)
                evl5_cnt = reviewEvl["5"]
                evl4_cnt = reviewEvl["4"]
                evl3_cnt = reviewEvl["3"]
                evl2_cnt = reviewEvl["2"]
                evl1_cnt = reviewEvl["1"]
                god_nm = goods[0].god_nm
                sentiword_goods_score(id=id,power_negative=power_negative, negative=negative, neutrality=neutrality, positive=positive,
                                power_positive=power_positive,god_no=god_no, total=total,
                                evl5_cnt=evl5_cnt, evl4_cnt=evl4_cnt, evl3_cnt=evl3_cnt, evl2_cnt=evl2_cnt, evl1_cnt=evl1_cnt, god_nm=god_nm).save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'DELETE', 'PUT'])
def getSentiwordScore(request, key):
    # print(liveChatData)
    if request.method == 'GET':
        if key == "live":
            liveChatData = sentiword_live_score.objects.values()
            serializer = SentiWordLiveScoreSerializer(liveChatData, many=True)
        elif key=="goods":
            goodsReviewData = sentiword_goods_score.objects.values()
            serializer = SentiWordGoodsScoreSerializer(goodsReviewData, many=True)
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
                print(wordname)
                root, score = ksl.data_list(wordname)
                score = str(score)
                dic[score] = dic[score]+1
                # print(dic)
    return dic

@api_view(['GET','POST', 'DELETE', 'PUT'])
def getGoodsIdEvl(request, id, key):
    print(request.method)
    if request.method == 'GET':
        bestReview = {"5":0, "4":0, "3":0, "2":0, "1":0}
        goodsBestReview = god_god_evl.objects.filter(god_no=id)
        goodsReview = sentiword_goods_score.objects.filter(god_no=id)
        goodsImg = god_img.objects.filter(god_no=id).filter(img_turn=0)
        if len(goodsImg) == 0:
            goodsImg = god_img.objects.filter(god_no=id).filter(img_turn=1)
        # goods = god.objects.filter(god_no=id)
        # print(goods.god_nm)
        # print(goods[0].god_nm)
        for review in goodsBestReview:
            # print(review.tot_evl_score)
            if review.BST_GOD_EVL_YN == "Y":
                bestReview[review.tot_evl_score]+=1
        # print(bestReview)
        item = [{'id': id,
                 'power_negative':goodsReview[0].power_negative,
                 'negative' : goodsReview[0].negative,
                 'neutrality' : goodsReview[0].neutrality,
                 'positive' : goodsReview[0].positive,
                 'power_positive' : goodsReview[0].power_positive,
                 'god_no' : id,
                 'total' : goodsReview[0].total,
                 'evl5_cnt' : goodsReview[0].evl5_cnt,
                 'evl4_cnt' : goodsReview[0].evl4_cnt,
                 'evl3_cnt' : goodsReview[0].evl3_cnt,
                 'evl2_cnt' : goodsReview[0].evl2_cnt,
                 'evl1_cnt' : goodsReview[0].evl1_cnt,
                 'best_evl5_cnt': bestReview['5'],
                 'best_evl4_cnt': bestReview['4'],
                 'best_evl3_cnt': bestReview['3'],
                 'best_evl2_cnt': bestReview['2'],
                 'best_evl1_cnt': bestReview['1'],
                 'god_nm' : goodsReview[0].god_nm,
                 'god_img' : goodsImg[0].img_url
                }]
        serializer = GoodsEmotionSerializer(item, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

# DB에 없는 테이블 조합해서 json으로 부를떄
@api_view(['GET','POST', 'DELETE', 'PUT'])
def getGoodsEvl(request, key):
    print(request.method)
    if request.method == 'GET':
        bestReview = {"5":0, "4":0, "3":0, "2":0, "1":0}
        goodsReviewData = sentiword_goods_score.objects.values()
        # goods = god.objects.filter(god_no=id)
        # print(goods.god_nm)
        # print(goods[0].god_nm)
        items = []
        for review in goodsReviewData:
            # print(review.tot_evl_score)
            # print(review)
            goodsId = review['god_no']
            goodsIdReview = god_god_evl.objects.filter(god_no=goodsId)
            goodsReview = sentiword_goods_score.objects.filter(god_no=goodsId)
            goodsImg = god_img.objects.filter(god_no=goodsId).filter(img_turn=0)
            if len(goodsImg) == 0:
                goodsImg = god_img.objects.filter(god_no=goodsId).filter(img_turn=1)
            for r in goodsIdReview:
                if r.BST_GOD_EVL_YN == "Y":
                    bestReview[r.tot_evl_score]+=1
            item = {'id': goodsId, 
                    'power_negative':goodsReview[0].power_negative,
                    'negative' : goodsReview[0].negative,
                    'neutrality' : goodsReview[0].neutrality,
                    'positive' : goodsReview[0].positive,
                    'power_positive' : goodsReview[0].power_positive,
                    'god_no' : goodsId,
                    'total' : goodsReview[0].total,
                    'evl5_cnt' : goodsReview[0].evl5_cnt,
                    'evl4_cnt' : goodsReview[0].evl4_cnt,
                    'evl3_cnt' : goodsReview[0].evl3_cnt,
                    'evl2_cnt' : goodsReview[0].evl2_cnt,
                    'evl1_cnt' : goodsReview[0].evl1_cnt,
                    'best_evl5_cnt': bestReview['5'],
                    'best_evl4_cnt': bestReview['4'],
                    'best_evl3_cnt': bestReview['3'],
                    'best_evl2_cnt': bestReview['2'],
                    'best_evl1_cnt': bestReview['1'],
                    'god_nm' : goodsReview[0].god_nm,
                    'god_img' : goodsImg[0].img_url}
            items.append(item)
        # print(items)
        serializer = GoodsEmotionSerializer(items, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)