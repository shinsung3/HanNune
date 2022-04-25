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
                                        <v-card-actions class="pa-4">
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
                                    </v-col>
                                </div>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-container>
            </v-card>
        </v-app>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name:"goodsList",
    data: () => ({
        items: [],
        reviewTotCnt:[],
        review:[],
    }),
    created(){
        this.selectGod()
    },
    methods:{
        selectGod(){
            axios.get("http://127.0.0.1:8000/emotion/goods/score/")
            .then((result)=>{
                console.log("goods>>> ", result.data)
                for(var i =0; i<result.data.length; i++){
                    var color = "#F8BBD0";
                    var rColor = "red";
                    if(i%2!=0){
                        color = "#9DC3E6";
                        rColor = "red"
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
                        // show: true,
                        totCnt: result.data[i].evl1_cnt+result.data[i].evl2_cnt+result.data[i].evl3_cnt+result.data[i].evl4_cnt+result.data[i].evl5_cnt,
                        customerCnt: parseInt(((result.data[i].evl1_cnt*1+result.data[i].evl2_cnt*2+result.data[i].evl3_cnt*3+result.data[i].evl4_cnt*4+result.data[i].evl5_cnt*5)/
                                        (result.data[i].evl1_cnt+result.data[i].evl2_cnt+result.data[i].evl3_cnt+result.data[i].evl4_cnt+result.data[i].evl5_cnt))*100)/100,
                    })
                    // console.log(this.items[i].godNo)
                    // this.selectGodReviewRatio(this.items[i].godNo)
                    this.selectGodTotCnt(this.items[i].godNo, i)
                }
                // console.log(this.review)
            })
        },
        selectGodTotCnt(godNo){
            axios.get("http://127.0.0.1:8000/review/"+godNo+"/cnt")
            .then((result)=>{
                // console.log("totCnt>>> ",result.data)
                this.reviewTotCnt.push({
                    totCnt : result.data[0].god_evl_turn,
                    godNo : godNo
                })
            })
        },
        // selectGodReview(godNo, i){
        //     axios.get("http://127.0.0.1:8000/emotion/goods/score/"+godNo)
        //     .then((result)=>{

        //         console.log("비율>>> ",result.data)
        //         this.review.push({
        //             evl1_cnt: result.data[0].evl1_cnt,
        //             evl2_cnt: result.data[0].evl2_cnt,
        //             evl3_cnt: result.data[0].evl3_cnt,
        //             evl4_cnt: result.data[0].evl4_cnt,
        //             evl5_cnt: result.data[0].evl5_cnt,
        //             god_no: godNo,
        //             id: godNo,
        //             negative: result.data[0].negative,
        //             power_negative: result.data[0].power_negative,
        //             neutrality: result.data[0].neutrality,
        //             power_positive: result.data[0].power_positive,
        //             positive: result.data[0].positive,
        //             total: result.data[0].total,
        //             color:color,
        //             ratingColor:rColor,
        //             show: true,
        //         })
        //     })
        // }
    }
}
</script>
<style>
.v-title {
    font-family: 'Do Hyeon', sans-serif;
}
</style>