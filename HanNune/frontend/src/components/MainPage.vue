<template>
  <section id="main">
    <v-row no-gutters>
      <v-img
        width="100%"
        src="../assets/3.jpg"
      >
        <v-theme-provider dark>
          <v-container fill-height>
            <v-row
              align="center"
              class="white--text mx-auto"
              justify="center"
            >
              <v-col
                class="white--text text-center"
                cols="12"
                tag="h1"
              >
                <span
                :class="[$vuetify.breakpoint.smAndDown ? 'display-1' : 'display-2']"
                  class="font-weight-light"
                >
                  FOR HANDSOME
                </span>

                <br>

                <span
                  :class="[$vuetify.breakpoint.smAndDown ? 'display-3': 'display-4']"
                  class="font-weight-black"
                >
                  HANUNE
                </span>

                <br>
                <span
                  :class="[$vuetify.breakpoint.smAndDown ? 'display-1': 'display-1']"
                  class="font-weight-black"
                >
                  - VITAMIN PLUS -
                </span>

              </v-col>

              <v-btn
                class="align-self-end"
                fab
                outlined
                @click="$vuetify.goTo('#about-me')"
              >
                <v-icon>mdi-chevron-double-down</v-icon>
              </v-btn>
            </v-row>
          </v-container>
        </v-theme-provider>
      </v-img>
    </v-row>
  </section>
</template>

<script>
  export default {
    name: 'MainPage',
  }
</script>
