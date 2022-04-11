<template>
  <v-app>
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex v-for="i in liveLen" :key="`3${i}`" xs3>
          <v-card
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

            <v-card-title>{{live[i-1].live_name}}</v-card-title>

            <v-card-text>
              <v-flex v-for="j in liveLen" :key="j">
                <v-row v-if="wordScore[j-1][0].live_id == live[i-1].live_id"
                  align="center"
                  class="mx-0"
                >

                    <v-rating
                      :value="parseInt(((wordScore[j-1][0].power_positive + wordScore[j-1][0].positive)/wordScore[j-1][0].total)*100)*5/100"
                      color="amber"
                      dense
                      half-increments
                      readonly
                      size="14"
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

            <v-card-title>HOT KEYWORD</v-card-title>

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
      hotKeyword:[]
    }),
    created() {
      this.liveDataSelect()
      // this.wordScoreSelect()
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
          }
          this.wordScoreSelect()
          console.log(this.wordScore)
          this.hotKeywordSelect()
          console.log(this.hotKeyword)
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
      hotKeywordSelect(){
        for(var i = 0; i<this.liveLen; i++){
          axios.get("http://127.0.0.1:8000/keyword/live/"+this.live[i].live_id)
          .then((result)=>{
            var temp = result.data
            this.hotKeyword.push(this.makeHotKeywordArray(temp))
            console.log(this.hotKeyword)
          })
        }
      },
      makeHotKeywordArray(arr){
        var tempArray = []

        tempArray.push({
          live_id: arr[0].live_id,
          params:{
            first: arr[0].keyword,
            second: arr[1].keyword,
            third: arr[2].keyword,
            forth: arr[3].keyword,
            fifth: arr[4].keyword,
            sixth: arr[5].keyword,
          }
        })

        return tempArray
      }
    },
  }
</script>