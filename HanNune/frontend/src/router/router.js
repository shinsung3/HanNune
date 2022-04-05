import Vue from 'vue'
import VueRouter from 'vue-router';
import HomePage from '@/components/HomePage';

import KeywordPage from '@/components/keyword/KeywordPage';
import EmotionPage from '@/components/emotion/EmotionMainPage';

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
      name: 'live',
      component: EmotionPage
    },
    {
      path:'/keyword',
      name:'keyword',
      component: KeywordPage
    }
  ]
});

export default router;