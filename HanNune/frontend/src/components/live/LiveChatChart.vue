<template>
    <div>
        <canvas id="live-chart"></canvas>
        {{ id }}
    </div>
</template>

<script>
import Chart from 'chart.js'
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

        console.log(this.liveChartData)
        this.makeChart(this.liveChartData)
    },
    methods:{
        setDataChart() {
            var chartData = {
                labels: this.timeArray,
                datasets: [{
                    label: 'My First dataset',
                    // backgroundColor: Utils.transparentize(Utils.CHART_COLORS.red, 0.5),
                    // borderColor: Utils.CHART_COLORS.red,
                    fill: false,
                    data: this.countArray,
                }]
            }

            return chartData
        },
        setLiveChartData(data){
            this.liveChartData = {
                type: 'line',
                data: data,
                options: {
                    plugins: {
                        title: {
                        text: 'Chart.js Time Scale',
                        display: true
                        }
                    },
                    scales: {
                        x: {
                            type: 'time',
                            time: {
                                unit: 'minute',
                                displayFormats: 'h:mm a'
                            },
                            display: true,
                            offset: true,
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'value'
                            }
                        }
                    },
                },
            }
        },
        makeChart(chartData){
            const ctx = document.getElementById('live-chart');
            new Chart(ctx, chartData);
        },
        makeGraphData(){
            var timestamp = []

            axios.get('http://127.0.0.1:8000/keyword/'+this.id)
            .then( result  => {
                // console.log("result : " + result)
                var raw = result.data
                // console.log(raw)
                timestamp = this.makeArray(raw)
                // console.log(timestamp)

                var index = Date.parse(timestamp[0].chatDt) // + Date(timestamp[0].chatDt).getMinutes
                var count = 1

                console.log(timestamp)

                for(var i=1; i < timestamp.length ; i++){
                  var tempTime = Date.parse(timestamp[i].chatDt)

                  if(index == tempTime){
                    count += 1
                  }else{
                    this.timeArray.push(new Date(index))
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