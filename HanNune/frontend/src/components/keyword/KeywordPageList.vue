<template>
    <v-app>
    <v-col>
      <header-page/>
    </v-col>
    <v-col>
      <p>이 페이지는 ID.{{ id }}의 상세를 출력합니다.</p>
      <!-- {{liveName}} -->
      <!-- {{imgUrl}} -->
      <!-- {{liveInfo}} -->
      <!-- {{this.$store.getters.getNumber()}} -->
      <!-- {{this.store.state.count}} -->
      {{n}}
      <div id="word-cloud"></div>
    </v-col>
    <footer-page/>
  </v-app>
</template>

<script>
import FooterPage from '../FooterPage.vue'
import HeaderPage from '../HeaderPage.vue'
import store from '@/store/emotionDetail'
import axios from 'axios'

const d3 = require("d3")
const width = 500;     
const height = 500;

var color = d3.scaleOrdinal(d3.schemeSet3);

  export default {
    data() {
        return {
            words: [],
        }
    },
    props:{
      id: String
    },
    computed: {
      n(){
        return store.state.n
      },
      hasResult: function() {
            return this.posts.length > 0
      }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/keyword/live/'+this.id)
            .then( (result)  => {
                var raw = result.data;
                this.words = this.makeKeywordArray(raw);
                console.log(this.words)
                this.genLayout()
            })
    },
    methods: {
        makeKeywordArray(arr){
            var tmpArray = [];
            for (var i = 0 ; i < arr.length; i++){
                tmpArray.push({
                    text: arr[i].keyword,
                    size: parseInt(parseFloat(arr[i].keyword_freq)/parseFloat(arr[0].keyword_freq) * 100)
                })
            }
            return tmpArray
        },

        genLayout() {
            const cloud = require('d3-cloud')
            cloud() // Cloud layout 생성
              .words(this.words) // layout에 넣을 단어들
              .padding(1) // 단어들의 사이 공간 좁게 (1)
              .font('Do Hyeon') // 폰트
              .fontSize((d) => {
                return d.size;
              }) // 폰트 크기 결정 words 내에 size 사용
              .on("end", this.end) // 배치가 끝나면 end 함수 부르기
              .spiral("archimedean")
              .start() // 배치 시작
              .stop(); // 계속 호출하지 않고 한번만 호출할 것이기 때문에 바로 stop()
        },

        end(words) {
            d3.select("#word-cloud")
                .append("svg")
                .attr("width", width)
                .attr("height", height)
                .style("background", "white")
                .attr("viewBox", "125 125 250 250")
                .append("g")
                .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")") // g를 중심에서 단어들을 그리기 때문에 g를 svg 중심으로 이동
                .selectAll("text")
                .data(words)
                .enter()
                .append("text")
                .style("font-family", 'Do Hyeon')
                .style("font-size", (d) => {
                    return d.size + "px";
                })
                .style("font-family", 'Do Hyeon')
                .style("fill", color)
                .attr("text-anchor", "middle")
                .attr("transform", (d) => {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .text((d) => d.text)
        },
    },
    components: { HeaderPage, FooterPage },
    name: 'live-detail',
  }
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&display=swap');
</style>