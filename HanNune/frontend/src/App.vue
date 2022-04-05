<template>
  <v-app>
    <router-view></router-view>
    <v-app-bar
      app
      color="#4395e0"
      height="75"
      dark
      elevation="5"
    >
    <div class="d-flex align-center">
      <v-img
        alt="Logo"
        class="shrink mr-2"
        contain
        src="./assets/white.png"
        width="63"
      ></v-img>
    </div>

      <v-toolbar-title class="font-weight-black headline">
        HANUNE
      </v-toolbar-title>
      <v-menu>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            v-bind="attrs"
            v-on="on"
            width="200"
            x-large
            text
            height="100"
          >
            HOME
          </v-btn>
        </template>
      </v-menu>
            <v-menu>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            v-bind="attrs"
            v-on="on"
            width="200"
            x-large
            text
            height="100"
          >
            H-GOODS
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="n in 5"
            :key="n"
            @click="() => {}"
          >
            <v-list-item-title>Option {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
      <!-- <v-menu> -->
        <router-link
          to="/live"
        >
        H-Live
        </router-link>
          <!-- <template v-slot:activator="{ on, attrs }"> -->

            <!-- <v-btn
            >
              H-LIVE
            </v-btn> -->
          <!-- </template> -->
        <!-- </router-link> -->

        <!-- <v-list>
          <v-list-item
            v-for="n in 5"
            :key="n"
            @click="() => {}"
          >
            <v-list-item-title>Option {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list> -->
      <!-- </v-menu> -->
    </v-app-bar>

    <v-main>
      <MainPage/>
      <PositiveNegativeRatio/>
      <HfmHotKeyword/>
    </v-main>
    <v-footer
      color="#9DC3E6"
      dark
    >
    <v-spacer></v-spacer>
    @COPYRIGHT VITAMIN PLUS - HANUNE [Hansome 2 Team] Nustar, HaSubin
    </v-footer>
  </v-app>
</template>

<script>
import MainPage from './components/MainPage';
import PositiveNegativeRatio from './components/PositiveNegativeRatio.vue';
import HfmHotKeyword from './components/HfmHotKeyword.vue';

export default {
  name: 'App',

  components: {
    MainPage,
    PositiveNegativeRatio,
    HfmHotKeyword,
  },

  data: () => ({
    //
  }),
};
</script>
