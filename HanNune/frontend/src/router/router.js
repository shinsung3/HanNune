import Vue from 'vue'
import VueRouter from 'vue-router';
import HomePage from '@/components/HomePage';

import KeywordPage from '@/components/keyword/KeywordPage';
import EmotionPage from '@/components/emotion/EmotionMainPage';
import LiveDetailPage from '@/components/emotion/LiveDetail';

Vue.use(VueRouter); // router 기능 확장 선언

const router = new VueRouter({
  mode: 'history',
  routes: [
    // 이곳에 router 를 등록
    {
      path:'/',
      name: 'main',
      component: HomePage
    },
    {
      path:'/live',
      name: 'live-list',
      component: EmotionPage
    },
    {
      path:'/live/detail', // ':id' 매개 변수에 들어 있는 경우, 값 라이브 방송에 따른 정보로 나뉨
      name: 'live-detail',
      component: LiveDetailPage,
      // 함수로 지정하면 첫 번째 매개변수로 현재 라우트 객체를 사용할 수 있음
      props: true,
      children:[
        {
          path:':id', // ':id' 매개 변수에 들어 있는 경우, 값 라이브 방송에 따른 정보로 나뉨
          name: 'live-detail',
          component: LiveDetailPage,
          // 함수로 지정하면 첫 번째 매개변수로 현재 라우트 객체를 사용할 수 있음
          props: true
        },
      ]
    },
    {
      path:'/keyword',
      name:'keyword',
      component: KeywordPage
    }
  ]
});

export default router;