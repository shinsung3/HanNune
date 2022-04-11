<template>
    <v-app>
        <div>
            <header-page/>
        </div>
        <div>
            <br>
            <br>
            <br>
            <br>
            <br>
            <div id="word-cloud"></div>
        </div>
        <footer-page/>
    </v-app>
</template>

<script>
import FooterPage from '../FooterPage.vue'
import HeaderPage from '../HeaderPage.vue'
import axios from 'axios'

var live_id = '1249'

  export default {
    components: { HeaderPage, FooterPage },
    name: 'KeywordPage',
    data() {
        return {
            words: [],
        }
    },
    computed: {
        hasResult: function() {
            return this.posts.length > 0
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/keyword/live/'+live_id)
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
                    size: parseInt(parseFloat(arr[i].keyword_freq)/parseFloat(arr[0].keyword_freq) * 50)
                })
            }
            return tmpArray
        },

        genLayout() {
            const cloud = require('d3-cloud')
            cloud() // Cloud layout 생성
              .words(this.words) // layout에 넣을 단어들
              .padding(1) // 단어들의 사이 공간 좁게 (1)
              .font("Impact") // 폰트
              .fontSize((d) => {
                return d.size;
              }) // 폰트 크기 결정 words 내에 size 사용
              .on("end", this.end) // 배치가 끝나면 end 함수 부르기
              .start() // 배치 시작
              .stop(); // 계속 호출하지 않고 한번만 호출할 것이기 때문에 바로 stop()
        },

        end(words) {
            const d3 = require("d3")
            const width = 300
            const height = 300

            d3.select("#word-cloud")
                .append("svg")
                .attr("width", width)
                .attr("height", height)
                .style("background", "white")
                .append("g")
                .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")") // g를 중심에서 단어들을 그리기 때문에 g를 svg 중심으로 이동
                .selectAll("text")
                .data(words)
                .enter()
                .append("text")
                .style("font-size", (d) => {
                    return d.size + "px";
                })
                .style("font-family", "Impact")
                .attr("text-anchor", "middle")
                .attr("transform", (d) => {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .text((d) => d.text)
        }
    }
 }
</script>