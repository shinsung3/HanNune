<template>
    <div>
        <canvas id="live-chart" style="height:300px; width:1000px"></canvas>
    </div>
</template>

<script>
import Chart from 'chart.js'
import 'chartjs-adapter-luxon'
import axios from 'axios'

export default {
    name: 'liveChartData',
    data() {
        return {
            timeArray : [],
            countArray : [],
            liveChartData: '',
        }
    },
    props:{
        id:String,
    },
    mounted() {
        this.makeGraphData()
        this.setLiveChartData(this.setDataChart())
        this.makeChart(this.liveChartData)
    },
    methods:{
        setDataChart() {
            var chartData = {
                labels: this.timeArray,
                datasets: [{
                    label: '채팅 수',
                    fill: true,
                    data: this.countArray,
                    borderColor: '#E1BEE7',
                    backgroundColor: 'rgba(225,190,231,0.5)',
                    borderWidth: 5
                }]
            }

            return chartData
        },
        setLiveChartData(data){
            this.liveChartData = {
                type: 'line',
                data: data,
                options: {
                    responsive:false,
                    legend: {
                        labels: {
                            fontColor: "black",
                            fontSize: 10,
                            display: false
                        }
                    },
                    scales: {
                        xAxes: [{
                            type: 'time',
                            time: {
                                unit: 'month'
                            }
                        }]
                    }
                },
            }
        },
        makeChart(chartData){
            const ctx = document.getElementById('live-chart');
            new Chart(ctx, chartData);
        },
        makeGraphData(){
            var timestamp = []

            axios.get('http://127.0.0.1:8000/live/'+this.id)
            .then( result  => {
                var raw = result.data
                timestamp = this.makeArray(raw)

                var index = Date.parse(timestamp[0].chatDt)
                var count = 1

                console.log(timestamp)

                for(var i=1; i < timestamp.length ; i++){
                  var tempTime = Date.parse(timestamp[i].chatDt)

                  if(index == tempTime){
                    count += 1
                  }else{
                    var tempTimestamp = new Date(index)

                    this.timeArray.push((tempTimestamp.toTimeString()).substr(0,5))
                    this.countArray.push(count)

                    index = index+60*1000
                    count = 0
                  }
                }

                console.log(this.timeArray)
                console.log(this.countArray)
            })
        },
        makeArray(chatData){
            var tempArray = []
            var arraySize = Object.keys(chatData).length
    
            for(var i = 0 ; i < arraySize ; i++){
                var tempDate = (chatData[i].live_chat_dt).substr(0,16)
        
                tempArray.push({
                    chatDt: new Date(tempDate),
                    chatCont: chatData[i].chat_cont
                })
            }

            return tempArray
        },

    }
}

</script>
<style scoped>

</style>