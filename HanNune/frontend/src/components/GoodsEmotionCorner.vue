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
            max-width="900"
          >
            <v-col class="font-weight-bold" id="fontColor">상품평 내 긍정지수가 높은 상품</v-col>
            <v-slide-group
              v-model="model2"
              class="pa-4"
              show-arrows
            >
              <v-slide-item
                v-for="(item, n) in sort"
                :key="n"
              >
                <v-card
                  class="ma-4"
                  height="280"
                  width="120"
                  elevation="0"
                >
                  <v-row
                    class="fill-height"
                    align="center"
                    justify="center"
                  >
                  <v-img :src="item.god_img_url"
                    class="white--text align-end"
                    gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.2)"
                    height="200px"
                  >
                    <v-avatar size="30" v-if="n==0">
                      <img
                        alt="user"
                        src="https://cdn-icons.flaticon.com/png/512/3212/premium/3212544.png?token=exp=1651050610~hmac=062558e5be4387fe9883554350a26ec2"
                      >
                    </v-avatar>
                    <v-avatar size="25" v-if="n==1">
                      <img
                        alt="user"
                        src="https://cdn-icons-png.flaticon.com/512/2583/2583319.png"
                      >
                    </v-avatar>
                    <v-avatar size="20" v-if="n==2">
                      <img
                        alt="user"
                        src="https://cdn-icons-png.flaticon.com/512/2583/2583434.png"
                      >
                    </v-avatar>
                    <!-- <v-card-subtitle v-text="item.godNm"></v-card-subtitle> -->
                    <!-- <v-card-text v-text="item.godNo"></v-card-text> -->
                    <div style="font-size:10px;">{{item.godNm}}
                      <p>{{item.godNo}}</p>
                    </div>
                  </v-img>
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
            <v-col class="font-weight-bold" id="fontColor">부정지수가 높은 상품</v-col>
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
import axios from 'axios';
  export default {
    name: 'PositiveNegativeRatio',
    data: () => ({
      sort:[],
      model:null,
      model2:null,
      items:[]
    }),
    created(){
      this.selectGod()
    },
    methods:{
      selectGod(){
        axios.get("http://127.0.0.1:8000/emotion/goods/total/score/")
        .then((result)=>{
            // console.log("goods>>> ", result.data)
            for(var i =0; i<result.data.length; i++){
                var color = "#F8BBD0";
                var rColor = "red";
                var bestRatingColor = "blue"
                var positiveColor = "teal darken-1"
                if(i%2!=0){
                    color = "#9DC3E6";
                }
                this.items.push({
                    godNm: result.data[i].god_nm,
                    godNo:result.data[i].god_no,
                    erpGodNo: result.data[i].erp_god_no,
                    evl1_cnt: result.data[i].evl1_cnt,
                    evl2_cnt: result.data[i].evl2_cnt,
                    evl3_cnt: result.data[i].evl3_cnt,
                    evl4_cnt: result.data[i].evl4_cnt,
                    evl5_cnt: result.data[i].evl5_cnt,
                    emotion: parseInt(((result.data[i].positive+result.data[i].power_positive)/
                                    (result.data[i].total))*100)*5/100,
                    best_evl1_cnt: result.data[i].best_evl1_cnt,
                    best_evl2_cnt: result.data[i].best_evl2_cnt,
                    best_evl3_cnt: result.data[i].best_evl3_cnt,
                    best_evl4_cnt: result.data[i].best_evl4_cnt,
                    best_evl5_cnt: result.data[i].best_evl5_cnt,
                    best_totCnt : result.data[i].best_evl5_cnt+result.data[i].best_evl4_cnt+result.data[i].best_evl3_cnt+result.data[i].best_evl2_cnt+result.data[i].best_evl1_cnt,
                    bestCnt : parseInt(((result.data[i].best_evl1_cnt*1+result.data[i].best_evl2_cnt*2+result.data[i].best_evl3_cnt*3+result.data[i].best_evl4_cnt*4+result.data[i].best_evl5_cnt*5)/
                                    (result.data[i].best_evl1_cnt+result.data[i].best_evl2_cnt+result.data[i].best_evl3_cnt+result.data[i].best_evl4_cnt+result.data[i].best_evl5_cnt))*100)/100,
                    bestRatingColor : bestRatingColor,
                    god_no: result.data[i].god_nm,
                    id: result.data[i].god_nm,
                    negative: result.data[i].negative,
                    power_negative: result.data[i].power_negative,
                    neutrality: result.data[i].neutrality,
                    power_positive: result.data[i].power_positive,
                    positive: result.data[i].positive,
                    total: result.data[i].total,
                    color:color,
                    ratingColor:rColor,
                    positiveColor : positiveColor,
                    // show: true,
                    totCnt: result.data[i].evl1_cnt+result.data[i].evl2_cnt+result.data[i].evl3_cnt+result.data[i].evl4_cnt+result.data[i].evl5_cnt,
                    customerCnt: parseInt(((result.data[i].evl1_cnt*1+result.data[i].evl2_cnt*2+result.data[i].evl3_cnt*3+result.data[i].evl4_cnt*4+result.data[i].evl5_cnt*5)/
                                    (result.data[i].evl1_cnt+result.data[i].evl2_cnt+result.data[i].evl3_cnt+result.data[i].evl4_cnt+result.data[i].evl5_cnt))*100)/100,
                    god_img_url : "https://cdn.hfashionmall.com"+result.data[i].god_img+"RGINL.jpg?RS=960x960&AR=0&CS=640x960"
                })
            }
          this.sort = this.items.sort(function(a,b){
            return a.emotion - b.emotion;
          })
          console.log(this.sort)
        })
      },
    }
  }
</script>
