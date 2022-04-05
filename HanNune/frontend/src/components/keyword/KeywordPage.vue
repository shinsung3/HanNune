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
        </v-div>
        <footer-page/>
    </v-app>
</template>

<script>
import FooterPage from '../FooterPage.vue'
import HeaderPage from '../HeaderPage.vue'
import axios from 'axios'

  export default {
    components: { HeaderPage, FooterPage },
    name: 'KeywordPage',
    data() {
        return {
            view: false,
            keyword: [],
            keyword_freq: []
        }
    },
    computed: {
        hasResult: function() {
            return this.posts.length > 0
        }
    },
    methods: {
        searchKeyword() {
            axios.get('http://127.0.0.1:8000/post/keyword/live/994/')
            .then( (result)  => {
                console.log(result.data)
            })

        }
    }
  }
</script>