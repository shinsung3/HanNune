<template>
  <v-app>
    <v-col>
      <header-page/>
    </v-col>
    <v-col>
      <live-emotion/>
    </v-col>
    <footer-page/>
  </v-app>
</template>

<script>
import FooterPage from '../FooterPage.vue'
import HeaderPage from '../HeaderPage.vue'
import LiveEmotion from './LiveEmotion.vue'
  export default {
  components: { HeaderPage, FooterPage, LiveEmotion },
    name: 'EmotionPage',
  }
</script>

