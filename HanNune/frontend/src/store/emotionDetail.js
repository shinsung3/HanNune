//store.js
import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios'

Vue.use(Vuex);

const store = new Vuex.Store({
    state:{
        n:101,
        textA: "textA",
        textB: "textB"
    },
    getters:{
    },
    mutations:{
        liveIdData(){
            axios.get("http://127.0.0.1:8000/live/")
            .then( (result)  => {
            this.liveLen = result.data.length
            for(var i = 0; i<result.data.length; i++){
                this.liveImgUrlArray[i] = result.data[i].live_img_url;
                this.live[i] = result.data[i];
                // console.log(this.live)
            }
            this.wordScoreSelect()
            // console.log(this.wordScore)
            this.hotKeywordSelect()
            console.log(this.hotKeyword)
            })
        }
    },
    action:{
    }
});

export default store