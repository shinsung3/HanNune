<template>
    <v-app>
    <v-col>
      <header-page/>
    </v-col>
    <v-col>
      <p>이 페이지는 ID.{{ id }}의 상세를 출력합니다.</p>
      <!-- {{liveName}} -->
      <!-- {{imgUrl}} -->
      <!-- {{liveInfo}} -->
      <!-- {{this.$store.getters.getNumber()}} -->
      <!-- {{this.store.state.count}} -->
      {{n}}
    </v-col>
    <footer-page/>
  </v-app>
</template>

<script>
import FooterPage from '../FooterPage.vue'
import HeaderPage from '../HeaderPage.vue'
import store from '@/store/emotionDetail'
  export default {
    computed: {
      n(){
        return store.state.n
      }
    },
    components: { HeaderPage, FooterPage },
    name: 'live-detail',
  }
</script>
