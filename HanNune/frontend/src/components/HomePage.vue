<template>
    <v-app>
        <Header/>
        <MainPage/>
        <GoodsEmotionCorner/>
        <HfmHotKeyword/>
        <Footer/>
    </v-app>
</template>

<script>
import MainPage from './MainPage';
import GoodsEmotionCorner from './GoodsEmotionCorner.vue';
import HfmHotKeyword from './HfmHotKeyword.vue';
import Header from './HeaderPage.vue';
import Footer from './FooterPage.vue';

export default {
  name: 'App',

  components: {
    Header,
    MainPage,
    GoodsEmotionCorner,
    HfmHotKeyword,
    Footer,
  },

  data: () => ({
  }),
};
</script>