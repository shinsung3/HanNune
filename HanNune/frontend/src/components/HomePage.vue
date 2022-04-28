<template>
    <v-app>
        <Header/>
        <MainPage/>
        <GoodsEmotion/>
        <HfmHotKeyword/>
        <Footer/>
    </v-app>
</template>

<script>
import MainPage from './MainPage';
import GoodsEmotion from './GoodsEmotion.vue';
import HfmHotKeyword from './HfmHotKeyword.vue';
import Header from './HeaderPage.vue';
import Footer from './FooterPage.vue';

export default {
  name: 'App',

  components: {
    Header,
    MainPage,
    GoodsEmotion,
    HfmHotKeyword,
    Footer,
  },

  data: () => ({
  }),
};
</script>