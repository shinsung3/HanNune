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
      </v-col>
    <footer-page/>
  </v-app>
</template>

<script>
import FooterPage from '../FooterPage.vue'
import HeaderPage from '../HeaderPage.vue'
import store from '@/store/emotionDetail'
import axios from 'axios'

  export default {
    data:()=>({
      live:[],
      wordScore:[],
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
    ],
    }),
    computed: {
      n(){
        return store.state.n
      }
    },
    created(){
      this.wordScoreSelect();
      this.liveIdData();
    },
    props: {
      id:String,
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
