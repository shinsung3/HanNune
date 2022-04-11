<template>
    <v-app>
    <v-col>
      <header-page/>
    </v-col>
    <v-col>
      <p>이 페이지는 ID.{{ id }}의 상세를 출력합니다.</p>
      {{liveName}}
      {{imgUrl}}
      {{liveInfo}}
    </v-col>
    <footer-page/>
  </v-app>
</template>

<script>
import FooterPage from '../FooterPage.vue'
import HeaderPage from '../HeaderPage.vue'
  export default {
    created() {
        console.log(this.name);
    },
    props: {
        id: String,
        name: String,
        imgUrl: String,
        liveInfo: Array
    },
    computed: {
        liveName: function () {
            return this.name
        }
    },
    components: { HeaderPage, FooterPage },
    name: 'live-detail',
  }
</script>
