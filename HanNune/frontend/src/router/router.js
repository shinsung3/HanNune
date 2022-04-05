import Vue from 'vue'
import VueRouter from 'vue-router';
import HomePage from '@/components/HomePage';
import EmotionPage from '@/components/emotion/EmotionPage';

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
    }
  ]
});

export default router;