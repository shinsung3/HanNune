<template>
    <div id="app">
        <v-app id="inspire">
            <v-card
                cols="12"
            >
                <v-container>
                    <v-row dense>
                        <v-col
                            v-for="(item, i) in items"
                            :key="i"
                        >
                            <v-card
                                :color="item.color"
                                dark
                            >
                                <div class="d-flex flex-no-wrap justify-space-between">
                                    <v-col cols="3">
                                        <v-avatar
                                            class="ma-1"
                                            width="200"
                                            height="400"
                                            tile
                                            >
                                            <!-- <v-img :src="item.src"></v-img> -->
                                            <v-img src="https://cdn.hfashionmall.com/goods/THBR/21/11/12/GM0121111299837_2_ORGINL.jpg?RS=960x960&AR=0&CS=640x960"></v-img>
                                        </v-avatar>
                                    </v-col>
                                    <v-col cols="7">
                                        <v-card-title
                                            class="text-h5"
                                            v-text="item.godNm"
                                        ></v-card-title>
                                        <v-card-subtitle v-text="item.godNo"></v-card-subtitle>
                                        <v-divider></v-divider>
                                        <!-- <v-card-text>{{item.erpGodNo}}</v-card-text> -->
                                        <!-- <v-card-actions> -->
                                            <!-- <v-btn
                                            v-if="item.artist === 'Ellie Goulding'"
                                            class="ml-2 mt-3"
                                            fab
                                            icon
                                            height="40px"
                                            right
                                            width="40px"
                                            >
                                            <v-icon>mdi-play</v-icon>
                                            </v-btn>
                                            <v-btn
                                            icon
                                            @click="item.show = !item.show"
                                            >
                                            <v-icon>{{ item.show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                                            </v-btn> -->
                                        <!-- </v-card-actions> -->
                                        <!-- <v-expand-transition> -->
                                        <v-card-actions>
                                                <!-- <v-divider></v-divider> -->
                                                <!-- <v-card-text> -->
                                                &nbsp;<span class="text--lighten-4 text-caption mr-2">고객 리뷰
                                                    <span class="font-weight-bold">
                                                        ({{item.totCnt}}개) 
                                                        &nbsp;<span style="color: #F44336;">{{item.customerCnt}}</span>
                                                    </span>
                                                </span>
                                                <v-rating ting
                                                :value="item.customerCnt"
                                                :background-color="item.ratingColor"
                                                :color="item.ratingColor"
                                                dense
                                                half-increments
                                                readonly
                                                size="20"
                                                ></v-rating>
                                                <!-- </v-card-text> -->
                                        <!-- </v-expand-transition> -->
                                        </v-card-actions>
                                        <v-card-actions>
                                                <!-- <v-divider></v-divider> -->
                                                <!-- <v-card-text> -->
                                                &nbsp;<span class="text--lighten-4 text-caption mr-2">베스트 리뷰
                                                    <span class="font-weight-bold">
                                                        ({{item.best_totCnt}}개)
                                                        &nbsp;<span style="color: #2196F3;">{{item.bestCnt}}</span>
                                                    </span>
                                                </span>
                                                <v-rating ting
                                                :value="item.bestCnt"
                                                :background-color="item.bestRatingColor"
                                                :color="item.bestRatingColor"
                                                dense
                                                half-increments
                                                readonly
                                                size="20"
                                                ></v-rating>
                                                <!-- </v-card-text> -->
                                        <!-- </v-expand-transition> -->
                                        </v-card-actions>
                                        <v-card-actions>
                                                <!-- <v-divider></v-divider> -->
                                                <!-- <v-card-text> -->
                                                &nbsp;<span class="text--lighten-4 text-caption mr-2">긍정 지수
                                                    <span class="font-weight-bold">
                                                        ({{item.total}}개)
                                                        &nbsp;<span style="color: #00897B;">{{item.emotion}}</span>
                                                    </span>
                                                </span>
                                                <v-rating ting
                                                :value="item.emotion"
                                                :background-color="item.positiveColor"
                                                :color="item.positiveColor"
                                                dense
                                                half-increments
                                                readonly
                                                size="20"
                                                ></v-rating>
                                                <!-- </v-card-text> -->
                                        <!-- </v-expand-transition> -->
                                        </v-card-actions>
                                        <!-- <router-link to="/goods/detail" style="text-decoration:none;"> -->
                                            <v-card-actions>
                                                <v-chip
                                                    class="ma-2"
                                                    color="#FFFFFF"
                                                    outlined
                                                    @click="moveDetailPage(i)"
                                                    >
                                                    <v-icon left>
                                                        mdi-label
                                                    </v-icon>
                                                    상품 분석 디테일 >
                                                </v-chip>
                                            </v-card-actions>
                                        <!-- </router-link> -->
                                    </v-col>
                                </div>
                            </v-card>
                        </v-col>
                        <!-- <v-dialog
                            v-model="dialog"
                            scrollable
                            max-width="300px"
                        >
                            <template v-slot:activator="{ on, attrs }">
                                <v-card-actions>
                                    <v-btn
                                        elevation="2"
                                        outlined
                                        v-bind="attrs"
                                        v-on="on"
                                        >비율분석
                                        {{dialog}}
                                    </v-btn>
                                </v-card-actions>
                            </template>
                            <v-card>
                                <v-card-title class="text-h5 grey lighten-2">
                                    Privacy Policy {{dialog}}
                                </v-card-title>
                                <v-card-text>
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                                </v-card-text>
                                <v-divider></v-divider>
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn
                                    color="primary"
                                    text
                                    @click="hideDialog"
                                    >
                                    {{dialog}}
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog> -->
                    </v-row>
                </v-container>
            </v-card>
            <div >
                <canvas id="myChart"></canvas>
            </div>

        </v-app>
    </div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.min.js"></script>
<script src="https://unpkg.com/vue-chartjs/dist/vue-chartjs.min.js"></script>
<script>
import axios from 'axios'
export default {
    name:"goodsList",
    data: () => ({
        items: [],
        reviewTotCnt:[],
        review:[],
        dialog: false,
        showDialog : false
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
                    })
                    const config =  {
                        type: "pie",
                        data: {
                        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
                        datasets: [
                            {
                            label: "# of Votes",
                            data: [this.items[0].evl1_cnt,this.items[0].evl2_cnt,this.items[0].evl3_cnt,this.items[0].evl4_cnt,this.items[0].evl5_cnt],
                            backgroundColor: [
                                "rgba(255, 99, 132, 0.2)",
                                "rgba(54, 162, 235, 0.2)",
                                "rgba(255, 206, 86, 0.2)",
                                "rgba(75, 192, 192, 0.2)",
                                "rgba(153, 102, 255, 0.2)",
                                "rgba(255, 159, 64, 0.2)",
                            ],
                            borderColor: [
                                "rgba(255,99,132,1)",
                                "rgba(54, 162, 235, 1)",
                                "rgba(255, 206, 86, 1)",
                                "rgba(75, 192, 192, 1)",
                                "rgba(153, 102, 255, 1)",
                                "rgba(255, 159, 64, 1)",
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
                    var ctx = document.getElementById("myChart")
                    var myChart = new Chart(ctx,config);
                }
                console.log(this.items)
                this.chartMethod()
            })
        },
        chartMethod(){
            // <block:actions:2>
            var ctx = document.getElementById("myChart")
            // .getContext("2d");
            console.log(ctx)
            const config =  {
                type: "pie",
                data: {
                labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
                datasets: [
                    {
                    label: "# of Votes",
                    data: [12, 19, 3, 5, 2, 3],
                    backgroundColor: [
                        "rgba(255, 99, 132, 0.2)",
                        "rgba(54, 162, 235, 0.2)",
                        "rgba(255, 206, 86, 0.2)",
                        "rgba(75, 192, 192, 0.2)",
                        "rgba(153, 102, 255, 0.2)",
                        "rgba(255, 159, 64, 0.2)",
                    ],
                    borderColor: [
                        "rgba(255,99,132,1)",
                        "rgba(54, 162, 235, 1)",
                        "rgba(255, 206, 86, 1)",
                        "rgba(75, 192, 192, 1)",
                        "rgba(153, 102, 255, 1)",
                        "rgba(255, 159, 64, 1)",
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
        moveDetailPage(idx){
            console.log(this.items[idx].godNo)
            this.$router.push({
                name : 'goods-detail',
                params: {
                    id: this.items[idx].godNo,
                    item : this.items[idx]
                }
            })
        }
    }
}
</script>
<style>
.v-title {
    font-family: 'Do Hyeon', sans-serif;
}
</style>