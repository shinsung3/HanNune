<template>
  <section id="positiveNegativeRatio">
    <div class="py-12"></div>

    <v-container class="text-center">
      <h2 class="display-2 font-weight-bold mb-3" id="fontColor">
        GOODS ANALYTICS</h2>

      <v-responsive
        class="mx-auto mb-8"
        width="350"
      >
        <v-divider
          class="mb-1 grey"
        ></v-divider>

        <v-divider class="grey"></v-divider>
      </v-responsive>

      <v-responsive
        class="mx-auto title font-weight-light mb-8"
      >
        <v-col>
          <v-sheet
            class="mx-auto"
            elevation="8"
            max-width="800"
          >
            <v-col class="font-weight-bold" id="fontColor">긍정 상품</v-col>
            <v-slide-group
              v-model="model2"
              class="pa-4"
              show-arrows
            >
              <v-slide-item
                v-for="n in 15"
                :key="n"
                v-slot="{ active, toggle }"
              >
                <v-card
                  :color="active ? 'primary' : 'grey lighten-1'"
                  class="ma-4"
                  height="200"
                  width="100"
                  @click="toggle"
                >
                  <v-row
                    class="fill-height"
                    align="center"
                    justify="center"
                  >
                    <v-scale-transition>
                      <v-icon
                        v-if="active"
                        color="white"
                        size="48"
                        v-text="'mdi-close-circle-outline'"
                      ></v-icon>
                    </v-scale-transition>
                  </v-row>
                </v-card>
              </v-slide-item>
            </v-slide-group>

            <v-expand-transition>
              <v-sheet
                v-if="model2 != null"
                height="200"
                tile
              >
                <v-row
                  class="fill-height"
                  align="center"
                  justify="center"
                >
                  <h3 class="text-h6">
                    긍정 {{ model2 }}
                  </h3>
                </v-row>
              </v-sheet>
            </v-expand-transition>
          </v-sheet>
        </v-col>
        <v-col>
          <v-sheet
            class="mx-auto"
            elevation="8"
            max-width="800"
          >
            <v-col class="font-weight-bold" id="fontColor">부정 상품</v-col>
            <v-slide-group
              v-model="model"
              class="pa-4"
              show-arrows
            >
              <v-slide-item
                v-for="n in 15"
                :key="n"
                v-slot="{ active, toggle }"
              >
                <v-card
                  :color="active ? 'primary' : 'grey lighten-1'"
                  class="ma-4"
                  height="200"
                  width="100"
                  @click="toggle"
                >
                  <v-row
                    class="fill-height"
                    align="center"
                    justify="center"
                  >
                    <v-scale-transition>
                      <v-icon
                        v-if="active"
                        color="white"
                        size="48"
                        v-text="'mdi-close-circle-outline'"
                      ></v-icon>
                    </v-scale-transition>
                  </v-row>
                </v-card>
              </v-slide-item>
            </v-slide-group>

            <v-expand-transition>
              <v-sheet
                v-if="model != null"
                height="200"
                tile
              >
                <v-row
                  class="fill-height"
                  align="center"
                  justify="center"
                >
                  <h3 class="text-h6">
                    부정 {{ model }}
                  </h3>
                </v-row>
              </v-sheet>
            </v-expand-transition>
          </v-sheet>
        </v-col>
      </v-responsive>

      <div></div>
    </v-container>

    <div class="py-12"></div>
  </section>
</template>

<style scoped>
  #fontColor{
    color:#686868;
  }
</style>

<script>
  export default {
    name: 'PositiveNegativeRatio',
    data: () => ({
      model: null,
      model2: null,
    }),
  }
</script>
