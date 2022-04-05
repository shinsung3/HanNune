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
from . import emotion_views, keyword_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.index_home, name='index'),

    #live
    path('live/', live_views.liveDataController, name="liveAllData"), #live전체 호출
    path('live/<int:live_id>', live_views.liveIdDataController, name="liveIdData"), #live_id로 호출

    #emotion
    path('emotion/', emotion_views.emotionController, name="emotion"), #chat전체 호출
    path('emotion/<int:live_id>/', emotion_views.emotionPKController, name="emotion_pk"), #live_id로 호출
    path('sentiword/<str:searchWord>/', emotion_views.sentiwordController, name="sentiwordSearch"), #live_id로 호출
    path('post/sentiword/live/<int:live_id>/', emotion_views.insertLiveChatSentiwordController, name="sentiwordSearch"), #live_id로 호출

    #keyword
    path('keyword/', keyword_views.keywordController, name="keyword"), #chat전체 호출
    path('keyword/<int:live_id>/', keyword_views.keywordPKController, name="keyword_pk"), #live_id로 호출
    path('post/keyword/live/<int:live_id>/', keyword_views.insertLiveChatKeywordController, name="keywordSearch"), #live_id로 호출
]
