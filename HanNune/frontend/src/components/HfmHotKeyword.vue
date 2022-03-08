<template>
    <section
        id="features"
        class="lighten-3"
        style="background-color:#FFD85B"
      >
        <div class="py-12"></div>

        <v-container class="text-center">
          <h2 class="display-2 font-weight-bold mb-3" style="color:#fff;">HFM HOT KEYWORD</h2>

          <v-responsive
            class="mx-auto mb-12"
            width="400"
          >
            <v-divider class="mb-1 white"></v-divider>

            <v-divider class="white"></v-divider>
          </v-responsive>

          <v-row>
            <v-col
              v-for="({ icon, title, text }, i) in features"
              :key="i"
              cols="12"
              md="4"
            >
              <v-card
                class="py-12 px-4"
                color="grey lighten-5"
                flat
              >
                <v-theme-provider dark>
                  <div>
                    <v-avatar
                      color="primary"
                      size="88"
                    >
                      <v-icon
                        large
                        v-text="icon"
                      ></v-icon>
                    </v-avatar>
                  </div>
                </v-theme-provider>

                <v-card-title
                  class="justify-center font-weight-black text-uppercase"
                  v-text="title"
                ></v-card-title>

                <v-card-text
                  class="subtitle-1"
                  v-text="text"
                >
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-container>

        <div class="py-12"></div>
    </section>
</template>
<script>
export default {
    name:'HfmHotKeyword',
    data:()=>({
        features: [
            {
                icon: 'mdi-account-group-outline',
                title: 'HOT KEYWORD',
                text: 'HOT KEYWORD',
            },
            {
                icon: 'mdi-update',
                title: 'HOT KEYWORD',
                text: 'HOT KEYWORD',
            },
            {
                icon: 'mdi-shield-outline',
                title: 'HOT KEYWORD',
                text: 'HOT KEYWORD',
            },
        ]
    })
}
</script>