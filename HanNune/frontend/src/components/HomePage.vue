<template>
    <v-app>
        <Header/>
        <MainPage/>
        <PositiveNegativeRatio/>
        <HfmHotKeyword/>
        <Footer/>
    </v-app>
</template>

<script>
import MainPage from './MainPage';
import PositiveNegativeRatio from './PositiveNegativeRatio.vue';
import HfmHotKeyword from './HfmHotKeyword.vue';
import Header from './HeaderPage.vue';
import Footer from './FooterPage.vue';

export default {
  name: 'App',

  components: {
    Header,
    MainPage,
    PositiveNegativeRatio,
    HfmHotKeyword,
    Footer,
  },

  data: () => ({
    //
  }),
};
</script>