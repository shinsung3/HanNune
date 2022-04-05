// index.js
import Vue from 'vue'
import VueRouter from 'vue-router';
import { MainPage } from '../components/MainPage.vue';
import { EmotionPage } from './components/emotion/EmotionPage.vue';

Vue.use(VueRouter); // router 기능 확장 선언

export default new VueRouter({
  mode: 'history',
  routes: [
    // 이곳에 router 를 등록
    {
      path:'/',
      name: 'main',
      component: MainPage
    },
    {
      path:'/live',
      name: 'live',
      component: EmotionPage
    }
  ]
})