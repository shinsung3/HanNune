<template>
    <v-app>
      <v-col>
        <v-row>
          <header-page/>
        </v-row>
      </v-col>
      <v-col>
        <v-row>
          <v-container grid-list-md text-xs-center>
            <v-layout row wrap>
              <v-flex style="padding: 50px;">
                <v-row
                  class="mx-auto my-12"
                >
                  <v-col cols="4">
                    <v-card>
                      <v-img height="600" :src="live[0].live_img_url" class="white--text align-end">
                      </v-img>
                    </v-card>
                  </v-col>
                  <v-col cols="8">
                    <v-card-text>
                      <span class="font-weight-bold ml-8 mb-2" style="font-size:large">
                        {{live[0].live_name}}
                      </span>
                      <br/>
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
                    </v-card-text>
                  </v-col>
                </v-row>
              </v-flex>
            </v-layout>
          </v-container>
        </v-row>
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
    data:()=>({
      live:[],
      wordScore:[],
      words:[],
      messages: [
      {
        from: '강한 긍정단어',
        // message: 'Did you still want to grab lunch today?',
        cnt: '',
        color: 'deep-purple lighten-1',
      },
      {
        from: '긍정단어',
        // message: `Sure, I'll see you later.`,
        cnt: '',
        color: 'deep-purple lighten-1',
      },
      {
        from: '강한 부정단어',
        // message: 'Yeah, sure. Does 1:00pm work?',
        cnt: '',
        color: 'green',
      },
      {
        from: '부정단어',
        // message: 'Did you still want to grab lunch today?',
        cnt: '',
        color: 'green',
      },
      {
        words: [],
      }
    ],
    }),
    computed: {
      n(){
        return store.state.n
      },
      hasResult: function() {
            return this.posts.length > 0
      }
    },
    created(){
      this.wordScoreSelect();
      this.liveIdData();
    },
    props: {
      id:String,
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
    components: { HeaderPage, FooterPage },
    name: 'live-detail',
    methods:{
      liveIdData(){
        // console.log(this.id);
        axios.get("http://127.0.0.1:8000/live/"+this.id)
        .then( (result)  => {
          // console.log(result.data)
          this.live = result.data;
        })
      },
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
      wordScoreSelect(){
        axios.get("http://127.0.0.1:8000/emotion/live/score/"+this.id)
        .then((result)=>{
          this.wordScore.push(result.data);
          console.log(result.data)
          this.messages[0].cnt = this.wordScore[0][0].power_positive;
          this.messages[1].cnt = this.wordScore[0][0].positive;
          this.messages[2].cnt = this.wordScore[0][0].power_negative;
          this.messages[3].cnt = this.wordScore[0][0].negative;
        })
      },
    }
  }
</script>
