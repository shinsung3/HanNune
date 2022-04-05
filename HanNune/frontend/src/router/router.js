import Vue from 'vue'
import VueRouter from 'vue-router';
// import { MainPage } from './components';
import EmotionPage from '@/components/emotion/EmotionPage';

Vue.use(VueRouter); // router 기능 확장 선언

const router = new VueRouter({
  // mode: 'history',
  routes: [
    // 이곳에 router 를 등록
    // {
    //   path:'/',
    //   name: 'main',
    //   component: MainPage
    // },
    {
      path:'/live',
      name: 'live',
      component: EmotionPage
    }
  ]
});

export default router;