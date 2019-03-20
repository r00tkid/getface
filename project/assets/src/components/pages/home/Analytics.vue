<template>
    <v-layout row wrap justify-start v-show="getAnalytics">
        <v-flex lg6 xs12>
            <v-layout row wrap justify-start>
                <div class="mainChartContainer">
                    <line-chart :chart_data="chartData" :chart_options="chartOptions" :chart_render="getAnalytics"/>
                </div>
            </v-layout>
        </v-flex>
        <v-flex lg6 xs12>
            <v-layout>
                <v-flex lg6 class="mainStat">
                    <home-stat></home-stat>
                </v-flex>
                <v-flex lg6>
                    <home-time-table></home-time-table>
                </v-flex>
            </v-layout>
        </v-flex>
    </v-layout>
</template>

<script>
    import {createNamespacedHelpers} from 'vuex';
    import LineChart from "../../charts/Chart";
    import HomeTimeTable from "./analytics/HomeTimeTable";
    import HomeStat from "./analytics/HomeStat";

    const {mapState} = createNamespacedHelpers('session/pages/main');

    export default {
        name: "get-face-home-analytics",
        data() {
            return {
                chartData: {
                    datasets: [
                        {
                            label: "Data One",
                            backgroundColor: "#5ae08f",
                            borderColor: "#5ae08f",
                            lineTension: 0,
                            data: [
                                {x: "01/07/18", y: 25},
                                {x: "01/08/18", y: 35},
                                {x: "01/09/18", y: 15},
                                {x: "01/10/18", y: 20},
                                {x: "01/11/18", y: 40},
                                {x: "01/12/18", y: 30}
                            ],
                            fill: false
                        },
                        {
                            label: "Data One",
                            backgroundColor: "#fbbd21",
                            borderColor: "#fbbd21",
                            lineTension: 0,
                            data: [
                                {x: "01/07/18", y: 10},
                                {x: "01/08/18", y: 55},
                                {x: "01/09/18", y: 30},
                                {x: "01/10/18", y: 20},
                                {x: "01/11/18", y: 46},
                                {x: "01/12/18", y: 60}
                            ],
                            fill: false
                        }
                    ]
                },
                chartOptions: {
                    responsive: true,
                    maintainAspectRatio: false,
                    layout: {
                        margin: {
                            left: -50,
                            right: 0,
                            top: 0,
                            bottom: 0
                        }
                    },
                    scales: {
                        xAxes: [
                            {
                                type: "time",
                                time: {
                                    unit: "month",
                                    format: "DD/MM/YYYY",
                                    tooltipFormat: "ll"
                                }
                            }
                        ],
                        yAxes: [
                            {
                                ticks: {
                                    max: 100
                                }
                            }
                        ]
                    },
                    legend: {
                        display: false
                    },
                    tooltips: {
                        cornerRadius: 2,
                        callbacks: {
                            label: tooltipItem => `${tooltipItem.yLabel}: ${tooltipItem.xLabel}`,
                            title: () => null
                        }
                    }
                }
            }
        },
        components: {
            HomeTimeTable,
            LineChart,
            HomeStat,
        },
        computed: {
            ...mapState({
                getAnalytics: state => state.showAnalytics,
            }),
        },
    }
</script>

<style scoped>
    .mainChartContainer {
        width: 100%;
    }
</style>