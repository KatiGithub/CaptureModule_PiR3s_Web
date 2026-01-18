<template>
    <q-card class="my-card">
        <q-card-section>
            <div class="row items-center q-mb-md">
                <div class="text-h6 q-mr-md">Chart</div>

                <div class="row items-center bg-grey-2 rounded-borders q-px-sm q-py-xs">
                    <q-icon name="circle" color="positive" size="xs" class="q-mr-xs" v-if="RxLinkStatus" />
                    <q-icon name="circle" color="negative" size="xs" class="q-mr-xs" v-if="!RxLinkStatus" />
                    <span class="text-caption text-grey-8">Rx Link</span>
                </div>
            </div>

            <apexchart height="370" type="bar" :options="chartOptions" :series="series"></apexchart>
        </q-card-section>
    </q-card>
</template>

<script lang="ts">
/* eslint-disable */

import { defineComponent } from 'vue';
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
    data() {
        const series = [{
            name: 'Data',
            data: [10, 20, 30, 40]
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

        const RxLinkStatus = false

        return { series, chartOptions, RxLinkStatus };
    },
    methods: {
        getChartInfo() {
            axios.get('http://192.168.1.100:8080/api/status')
                .then((val) => {
                    console.log(val)
                    const response_body = val.data;
                    console.log(response_body)
                    console.log(this.series)
                    this.series[0]["data"][0] = response_body["tcpPacketsCount"]
                    this.series[0]["data"][1] = response_body["arpPacketsCount"]
                    this.series[0]["data"][2] = response_body["udpPacketsCount"]
                    this.series[0]["data"][3] = response_body["otherPacketsCount"]

                    this.RxLinkStatus = response_body["loggingPortStatus"]

                    setTimeout(() => {
                        this.getChartInfo();
                    }, 200)
                })
        },
    }
})
</script>