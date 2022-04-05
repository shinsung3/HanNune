import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from '@/router/router';

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  vuetify,
  router, // router 추가
}).$mount('#app')