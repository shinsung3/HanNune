<template>
    <v-app>
      <!-- <v-col> -->
        <!-- <v-row> -->
          <header-page/>
        <!-- </v-row> -->
      <!-- </v-col> -->
      <v-col style="padding:100px 50px;" cols="12">
        <v-card>
        <v-container>
          <v-row dense>
            <!-- <div> -->
              <!-- <v-card> -->
                <v-col cols="4">
                  <v-avatar
                      class="ma-1"
                      width="350"
                      height="500"
                      tile
                      >
                      <v-img :src="items[0].god_img_url"></v-img>
                  </v-avatar>
                  <v-timeline
                    align-top
                    dense
                  >
                    <v-timeline-item
                      v-for="message in messages"
                      :key="message.time"
                      :color="message.color"
                      small
                    >
                      <div>
                        <div class="font-weight-normal">
                          <strong>{{ message.from }}</strong> {{ message.cnt }}개
                        </div>
                        <!-- <div>{{ message.message }}</div> -->
                      </div>
                    </v-timeline-item>
                  </v-timeline>
                </v-col>
              <!-- </v-card> -->
              <!-- <v-card> -->
                <v-col cols="8">
                  <v-card-title>{{items[0].godNm}}</v-card-title>
                  <v-card-subtitle class="grey--text">{{items[0].godNo}}</v-card-subtitle>
                  <v-expansion-panels  on-panels
                    multiple
                  >
                    <v-expansion-panel>
                      <v-expansion-panel-header @click.native="makeChart"
                        color="#73AEFC"
                        style="color:#fff"
                      >
                        상품평 단어별 긍정 / 부정 단어 비율
                      </v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <div>
                            <canvas id="myChart"></canvas>
                        </div>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header
                        color="#F9B1B2"
                        style="color:#fff"
                      >Panel 2</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        Some content
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Panel 3</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        Some content
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                  </v-expansion-panels>
                </v-col>
              <!-- </v-card> -->
            <!-- </div> -->
          </v-row>
        </v-container>
        </v-card>
      </v-col>
    <footer-page/>
  </v-app>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.min.js"></script>
<script src="https://unpkg.com/vue-chartjs/dist/vue-chartjs.min.js"></script>
<script>
import FooterPage from '../FooterPage.vue'
import HeaderPage from '../HeaderPage.vue'
import axios from 'axios'

  export default {
    data:()=>({
      items:[],
      messages: [
        {
          from: '강한 긍정단어',
          // message: 'Did you still want to grab lunch today?',
          cnt: '',
          color: '#F9B1B2',
        },
        {
          from: '긍정단어',
          // message: `Sure, I'll see you later.`,
          cnt: '',
          color: '#F9B1B2',
        },
        {
          from: '강한 부정단어',
          // message: 'Yeah, sure. Does 1:00pm work?',
          cnt: '',
          color: '#FFD85B',
        },
        {
          from: '부정단어',
          // message: 'Did you still want to grab lunch today?',
          cnt: '',
          color: '#FFD85B',
        }
      ],
    }),
    computed: {
    },
    created(){
      this.goods()
      this.waitPage()
    },
    props: {
      id:String,
    },
    mounted() {
    },
    components: { HeaderPage, FooterPage },
    name: 'goods-detail',
    methods:{
      goods(){
        axios.get("http://127.0.0.1:8000/emotion/goods/total/score/"+this.id)
        .then((result)=>{
          var i = 0
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
            id: result.data[i].god_nm,
            negative: result.data[i].negative,
            power_negative: result.data[i].power_negative,
            neutrality: result.data[i].neutrality,
            power_positive: result.data[i].power_positive,
            positive: result.data[i].positive,
            total: result.data[i].total,
            // show: true,
            totCnt: result.data[i].evl1_cnt+result.data[i].evl2_cnt+result.data[i].evl3_cnt+result.data[i].evl4_cnt+result.data[i].evl5_cnt,
            customerCnt: parseInt(((result.data[i].evl1_cnt*1+result.data[i].evl2_cnt*2+result.data[i].evl3_cnt*3+result.data[i].evl4_cnt*4+result.data[i].evl5_cnt*5)/
                            (result.data[i].evl1_cnt+result.data[i].evl2_cnt+result.data[i].evl3_cnt+result.data[i].evl4_cnt+result.data[i].evl5_cnt))*100)/100,
            god_img_url : "https://cdn.hfashionmall.com"+result.data[i].god_img+"RGINL.jpg?RS=960x960&AR=0&CS=640x960"
          })
          this.messages[0].cnt = this.items[0].power_positive;
          this.messages[1].cnt = this.items[0].positive;
          this.messages[2].cnt = this.items[0].power_negative;
          this.messages[3].cnt = this.items[0].negative;
          console.log(this.items)
          // this.makeChart()
        })
      },
      makeChart(){
        // <block:actions:2>
        // this.chartHeight = "1500"
        // this.chartWidth = "700"
        var ctx = document.getElementById("myChart")
        // .getContext("2d");
        console.log(ctx)
        const config =  {
            type: "pie",
            data: {
            labels: ["강한부정", "부정", "긍정", "강한긍정"],
            datasets: [
                {
                label: "# of Votes",
                data: [this.items[0].power_negative, this.items[0].negative, this.items[0].positive, this.items[0].power_positive],
                backgroundColor: [
                    "rgba(255, 99, 132, 0.2)",
                    "rgba(255, 206, 86, 0.2)",
                    "rgba(75, 192, 192, 0.2)",
                    "rgba(153, 102, 255, 0.2)",
                    // "rgba(255, 159, 64, 0.2)",
                    // "rgba(54, 162, 235, 0.2)",
                ],
                borderColor: [
                    "rgba(255,99,132,1)",
                    "rgba(255, 206, 86, 1)",
                    "rgba(75, 192, 192, 1)",
                    "rgba(153, 102, 255, 1)",
                    // "rgba(255, 159, 64, 1)",
                    // "rgba(54, 162, 235, 1)",
                ],
                borderWidth: 1,
                },
            ],
            },
            options: {
            maintainAspectRatio: true, // default value. false일 경우 포함된 div의 크기에 맞춰서 그려짐.
            scales: {
                yAxes: [
                {
                    ticks: {
                    beginAtZero: true,
                    },
                },
                ],
            },
            },
        };
        var myChart = new Chart(ctx,config);
      },
      makeChart2(){
        // <block:actions:2>
        // this.chartHeight = "1500"
        // this.chartWidth = "700"
        var ctx = document.getElementById("myChart2")
        // .getContext("2d");
        console.log(ctx)
        const config =  {
            type: "pie",
            data: {
            labels: ["강한부정", "부정", "긍정", "강한긍정"],
            datasets: [
                {
                label: "# of Votes",
                data: [this.items[0].power_negative, this.items[0].negative, this.items[0].positive, this.items[0].power_positive],
                backgroundColor: [
                    "rgba(255, 99, 132, 0.2)",
                    "rgba(255, 206, 86, 0.2)",
                    "rgba(75, 192, 192, 0.2)",
                    "rgba(153, 102, 255, 0.2)",
                    // "rgba(255, 159, 64, 0.2)",
                    // "rgba(54, 162, 235, 0.2)",
                ],
                borderColor: [
                    "rgba(255,99,132,1)",
                    "rgba(255, 206, 86, 1)",
                    "rgba(75, 192, 192, 1)",
                    "rgba(153, 102, 255, 1)",
                    // "rgba(255, 159, 64, 1)",
                    // "rgba(54, 162, 235, 1)",
                ],
                borderWidth: 1,
                },
            ],
            },
            options: {
            maintainAspectRatio: true, // default value. false일 경우 포함된 div의 크기에 맞춰서 그려짐.
            scales: {
                yAxes: [
                {
                    ticks: {
                    beginAtZero: true,
                    },
                },
                ],
            },
            },
        };
        var myChart = new Chart(ctx,config);
      },
    }
  }
</script>
<style>
</style>