
<template>
    <q-card class="my-card">
        <q-card-section>
            <div class="text-h6">Chart</div>
            <apexchart 
             height="370"
             type="bar"
             :options="chartOptions"
             :series="series"
             ></apexchart>
        </q-card-section>
    </q-card>
</template>

<script lang="ts">
/* eslint-disable */

import {defineComponent} from 'vue';
import VueApexCharts from 'vue3-apexcharts';
import axios from 'axios';

    export default defineComponent({
        name: "Chart",
        components: {
            apexchart: VueApexCharts,
        },
        mounted() {
            this.getChartInfo();
        },
        data () {
            const series = [{
                name: 'Data',
                data: [10,20,30,40]
            }]
            const chartOptions = {
                chart: {
                    id: 'traffic-chart',
                    type: 'bar' as const,
                },

                plotOptions: {
                    bar: {
                        distributed: true
                    }
                },

                xaxis: { 
                    categories: ['TCP', 'ARP', 'UDP', 'Others']
                },
                colors: ['#64B98D', '#EDE07D', '#ED917E', '#6490B9']
            }
            return {series, chartOptions};
        },
        methods: {
            getChartInfo() {
                axios.get('http://127.0.0.1:5000/api/status')
                    .then((val) => {
                        console.log(val)
                        const response_body = val.data;
                        console.log(response_body)
                        console.log(this.series)
                        this.series[0]["data"][0] = response_body["tcpPacketsCount"]
                        this.series[0]["data"][1] = response_body["arpPacketsCount"]
                        this.series[0]["data"][2] = response_body["udpPacketsCount"]
                        this.series[0]["data"][3] = response_body["totalPacketsCount"]

                        setTimeout(() => {
                            this.getChartInfo();
                        }, 1000)
                    })
            },
        }
    })
</script>