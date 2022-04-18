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
                              <strong>{{ message.from }}</strong> @{{ message.time }}
                            </div>
                            <div>{{ message.message }}</div>
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
      messages: [
      {
        from: 'You',
        message: `Sure, I'll see you later.`,
        time: '10:42am',
        color: 'deep-purple lighten-1',
      },
      {
        from: 'John Doe',
        message: 'Yeah, sure. Does 1:00pm work?',
        time: '10:37am',
        color: 'green',
      },
      {
        from: 'You',
        message: 'Did you still want to grab lunch today?',
        time: '9:47am',
        color: 'deep-purple lighten-1',
      },
    ],
    }),
    computed: {
      n(){
        return store.state.n
      }
    },
    created(){
      this.liveIdData();
    },
    props: {
      id:String,
    },
    components: { HeaderPage, FooterPage },
    name: 'live-detail',
    methods:{
      liveIdData(){
        console.log(this.id);
        axios.get("http://127.0.0.1:8000/live/"+this.id)
        .then( (result)  => {
          console.log(result.data)
          this.live = result.data;
        })
      }
    }
  }
</script>
