<template>
  <v-app>
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex v-for="i in liveLen" :key="`3${i}`" xs3>
          <!-- <router-link style="text-decoration:none;" :to="{name : 'live-detail', params: {id: live[i-1].live_id, name: live[i-1].live_name}}" > -->
            <v-card
              @click="moveDetailPage(i-1)"
              :loading="loading"
              class="mx-auto my-12"
              max-width="374"
            >
              <template slot="progress">
                <v-progress-linear
                  color="deep-purple"
                  height="10"
                  indeterminate
                ></v-progress-linear>
              </template>

              <v-img
                height="250"
                :src="liveImgUrlArray[i-1]"
              ></v-img>

              <v-card-title class="v-title">{{live[i-1].live_name}}</v-card-title>

              <v-card-text class="v-title">
                <br/>
                <v-flex v-for="j in liveLen" :key="j">
                  <v-row v-if="wordScore[j-1][0].live_id == live[i-1].live_id"
                    align="center"
                    class="mx-0"
                  >
                긍정 지수 :
                      <v-rating
                        :value="parseInt(((wordScore[j-1][0].power_positive + wordScore[j-1][0].positive)/wordScore[j-1][0].total)*100)*5/100"
                        color="amber"
                        dense
                        half-increments
                        readonly
                        size=""
                      ></v-rating>

                      <div class="grey--text ms-4">
                        {{parseInt(((wordScore[j-1][0].power_positive + wordScore[j-1][0].positive)/wordScore[j-1][0].total)*100)*5/100}} ({{wordScore[i-1][0].total}})
                      </div>
                  </v-row>
                </v-flex>

                <!-- <div class="my-4 text-subtitle-1">
                  $ • Italian, Cafe
                </div> -->

                <!-- <div>Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating.</div> -->
              </v-card-text>

              <v-divider class="mx-4"></v-divider>
              <v-card-title class="v-keyword">HOT KEYWORD</v-card-title>

              <v-card-text>
                <v-chip-group
                  v-model="selection"
                  active-class="deep-purple accent-4 white--text"
                  column
                >
                  <v-chip>5:30PM</v-chip>
                  <v-chip>7:30PM</v-chip>
                  <v-chip>8:00PM</v-chip>
                  <v-chip>9:00PM</v-chip>
                  <v-chip>9:00PM</v-chip>
                  <v-chip>9:00PM</v-chip>
                </v-chip-group>
              </v-card-text>

              <v-card-actions>
                <v-btn
                  color="deep-purple lighten-2"
                  text
                  @click="reserve"
                >
                  Reserve
                </v-btn>
              </v-card-actions>
            </v-card>
          <!-- </router-link> -->
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
  import axios from 'axios'

  export default {
    data: () => ({
      liveImgUrlArray :[],
      live:[],
      loading: false,
      selection: 1,
      liveLen: 0,
      wordScore:[],
    }),
    created() {
      this.liveDataSelect()
      // this.wordScoreSelect()
    },
    computed: {
      list: () => this.live
    },
    methods: {
      reserve () {
        this.loading = true
        setTimeout(() => (this.loading = false), 2000)
      },
      liveDataSelect(){
        axios.get("http://127.0.0.1:8000/live/")
        .then( (result)  => {
          this.liveLen = result.data.length
          for(var i = 0; i<result.data.length; i++){
            this.liveImgUrlArray[i] = result.data[i].live_img_url;
            this.live[i] = result.data[i];
            console.log(this.live)
          }
          this.wordScoreSelect()
          console.log(this.wordScore)
        })
      },
      wordScoreSelect(){
        for(var i = 0; i<this.liveLen; i++){
          console.log(">>>>",i)
          axios.get("http://127.0.0.1:8000/emotion/live/score/"+this.live[i].live_id)
          .then((result)=>{
            this.wordScore.push(result.data);
          })
        }
      },
      moveDetailPage(idx){
        this.$router.push({
          name : 'live-detail',
          params: {
            id: this.live[idx].live_id,
            name: this.live[idx].live_name,
            imgUrl: this.live[idx].live_img_url,
            liveInfo: this.live[idx]
          }
        })
      }

    },
  }
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&display=swap');
.v-title {
 font-family: 'Do Hyeon', sans-serif;
}
.v-keyword{
  font-family: 'Black Han Sans', sans-serif;
}

</style>