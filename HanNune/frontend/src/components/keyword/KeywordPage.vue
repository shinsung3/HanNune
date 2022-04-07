<template>
    <v-app>
        <v-div>
            <header-page/>
        </v-div>
        <v-div>
            <br>
            <br>
            <br>
            <br>
            <br>
            <v-btn color="primary" @click="searchKeyword">get data</v-btn>
            <div v-for="(v, i) in keyword" :key="`${i}`">
                <p> keyword rank : {{ v.keyword_rank }} </p>
                <p> keyword : {{ v.keyword }} </p>
                <p> keyword freq : {{ v.keyword_freq }} </p>
            </div>
        </v-div>
        <footer-page/>
    </v-app>
</template>

<script>
import FooterPage from '../FooterPage.vue'
import HeaderPage from '../HeaderPage.vue'
import axios from 'axios'

var live_id = '994'

  export default {
    components: { HeaderPage, FooterPage },
    name: 'KeywordPage',
    data() {
        return {
            view: false,
            keyword: {
                live_id: '',
                keyword_rank:'',
                keyword: '',
                keyword_freq:''
            }
        }
    },
    computed: {
        hasResult: function() {
            return this.posts.length > 0
        }
    },
    created() {
        axios.get('http://127.0.0.1:8000/post/keyword/live/'+live_id)
            .then( (result)  => {
                this.keyword = result.data
            })
    },
    methods: {
        searchKeyword() {
            axios.get('http://127.0.0.1:8000/post/keyword/live/'+live_id)
            .then( (result)  => {
                console.log(result.data)
                this.keyword=result.data
                console.log(this.keyword)
            })
        }
    }
  }
</script>