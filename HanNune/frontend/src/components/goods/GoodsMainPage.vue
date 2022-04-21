<template>
  <v-app>
    <header-page/>
    <v-col style="padding:100px 50px;">
      <goods-list></goods-list>
    </v-col>
    <footer-page/>
  </v-app>
</template>

<script>
import FooterPage from '../FooterPage.vue'
import HeaderPage from '../HeaderPage.vue'
import GoodsList from './GoodsList.vue'
  export default {
  components: { HeaderPage, FooterPage, GoodsList },
    name: 'GoodsMainPage',
  }
</script>

