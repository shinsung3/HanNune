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
                            cols="12"
                        >
                            <v-card
                                :color="item.color"
                                dark
                            >
                                <div class="d-flex flex-no-wrap justify-space-between">
                                    <v-col cols="3">
                                        <v-avatar
                                            class="ma-1"
                                            width="250"
                                            height="350"
                                            tile
                                            >
                                            <!-- <v-img :src="item.src"></v-img> -->
                                            <v-img src="https://cdn.hfashionmall.com/goods/THBR/21/11/12/GM0121111299837_2_ORGINL.jpg?RS=960x960&AR=0&CS=640x960"></v-img>
                                        </v-avatar>
                                    </v-col>
                                    <v-col>
                                        <v-card-title
                                            class="text-h5"
                                            v-text="item.godNm"
                                        ></v-card-title>
                                        <v-card-subtitle v-text="item.godNo"></v-card-subtitle>
                                        <v-divider></v-divider>
                                        <!-- <v-card-text>{{item.erpGodNo}}</v-card-text> -->
                                        <v-card-actions>
                                            <v-btn
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
                                            </v-btn>
                                        </v-card-actions>
                                        <v-expand-transition>
                                            <div v-show="item.show">
                                                <!-- <v-divider></v-divider> -->
                                                <v-card-text>
                                                    긍정 리뷰 비율
                                                    {{item.reviewRatio}}
                                                </v-card-text>
                                            </div>
                                        </v-expand-transition>
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
        show1: true,
        items: [],
    }),
    created(){
        this.selectGod()
    },
    methods:{
        selectGod(){
            axios.get("http://127.0.0.1:8000/goods")
            .then((result)=>{
                console.log(result.data)
                for(var i =0; i<result.data.length; i++){
                    var color = "#F8BBD0";
                    if(i%2!=0){
                        color = "#9DC3E6";
                    }
                    this.items.push({
                        color: color,
                        godNm: result.data[i].god_nm,
                        godNo:result.data[i].god_no,
                        erpGodNo: result.data[i].erp_god_no,
                        show: true,
                        reviewRatio:0
                    })
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