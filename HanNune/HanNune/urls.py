"""HanNune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import emotion_views, keyword_views, live_views, goods_views, goods_review_views, sentiword_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.index_home, name='index'),

    #live
    path('live/', live_views.getLiveInfo, name="getLiveInfo"), #live 정보 전체 호출
    path('live/<int:live_id>', live_views.getLiveIdInfo, name="getLiveIdInfo"), #live_id 정보 호출
    path('live/chat', live_views.getLiveChat, name="getLiveChat"), #live chat전체 호출
    path('live/chat/<int:live_id>/', live_views.getLiveIdChat, name="getLiveIdChat"), #live chat live_id 기준으로 호출

    #emotion
    path('emotion/<str:key>/score/', emotion_views.getSentiwordScore, name="getSentiwordScore"), #live_id로 호출
    path('emotion/<str:key>/score/<str:id>/', emotion_views.getOrPostSentiwordScore, name="getOrPostSentiwordScore"), #live_id로 호출
    path('emotion/<str:key>/total/score/', emotion_views.getGoodsEvl, name="getGoodsEvl"), #god_no로 모든 리뷰 정보 호출
    path('emotion/<str:key>/total/score/<str:id>', emotion_views.getGoodsIdEvl, name="getGoodsIdEvl"), #god_no로 모든 리뷰 정보 호출

    #sentiword
    path('sentiword/<str:searchWord>/', sentiword_views.getSentiword, name="getSentiword"), #live_id로 호출

    #keyword
    path('keyword/<str:key>/rank/<str:id>', keyword_views.getOrPostKeywordRank, name="getOrPostKeywordRank"), #live_id로 호출

    #goods
    path('goods/', goods_views.goodsContoller, name="goods"), #goods 전체 호출

    #review
    path('review/<str:god_no>/', goods_review_views.getGoodsReview, name="getGoodsReview"), #god_no으로 리뷰 호출
    path('review/<str:god_no>/cnt', goods_review_views.getGoodsTotalCnt, name="getGoodsTotalCnt"), #god_no기준 리뷰 개수
]
