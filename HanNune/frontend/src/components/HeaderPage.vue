<template>
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
        src="../assets/white.png"
        width="63"
      ></v-img>
    </div>

      <router-link
        style="text-decoration:none; color:#fff;"
        to="/">
        <v-toolbar-title class="font-weight-black headline">
          HANUNE
        </v-toolbar-title>
      </router-link>
      <!-- <v-menu> -->
        <!-- <template v-slot:activator="{ on, attrs }"> -->
      <v-divider
        class="mx-4"
        vertical
      ></v-divider>
      <router-link
        style="text-decoration:none; color:#fff;"
        to="/">
        <v-btn
          width="200"
          x-large
          text
          height="100"
        >
          HOME
        </v-btn>
      </router-link>
        <!-- </template> -->
      <!-- </v-menu> -->
      <!-- <v-menu> -->
        <!-- <template v-slot:activator="{ on, attrs }"> -->
        <v-divider
        class="mx-4"
        vertical
      ></v-divider>
          <router-link
            style="text-decoration:none;"
            to="/goods">
          <v-btn
            width="200"
            x-large
            text
            height="100"
          >
            H-GOODS
          </v-btn>
          </router-link>
        <!-- </template> -->

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
      <!-- <v-menu> -->
          <!-- <template v-slot:activator="{ on, attrs }"> -->
      <v-divider
        class="mx-4"
        vertical
      ></v-divider>
        <router-link
          style="text-decoration:none;"
          to="/live">
            <v-btn
              width="200"
              x-large
              text
              height="100"
            >
              H-LIVE
            </v-btn>
          <!-- </template> -->
        </router-link>

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
</template>