<template>
    <v-container grid-list-md text-xs-center fluid class="home-wrap">
        <v-layout row wrap justify-end>
            <v-flex lg6 xs12 d-flex>
                <v-btn outline color="grey">23 янв 2019</v-btn>
                <v-btn outline color="grey">23 фев 2019</v-btn>
                <v-btn large outline color="grey">Сегодня</v-btn>
                <v-btn large outline color="grey">Неделя</v-btn>
                <v-btn large outline color="purple">Месяц</v-btn>
                <v-btn large outline color="grey">Год</v-btn>
            </v-flex>
        </v-layout>
        <v-layout row wrap justify-start>
            <v-flex lg6 xs12>
                <v-layout row wrap justify-start>
                    <v-flex xs12>
                        <v-layout align-content-start column>
                            <v-flex style="text-align: left;">
                                <v-btn color="#fa6d6e" dark class="hideAnalitics">Скрыть аналитику</v-btn>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                </v-layout>
            </v-flex>
            <v-flex lg6 xs12>
                <v-layout>
                    <v-flex lg2 xs12>
                        <v-card class="kill-card mt-3" dense>
                            <v-layout row justify-center>
                                <v-flex xs12>
                                    <v-card-title class="justify-center">
                                        <div class="headline">Разница
                                            <br>План/Факт
                                        </div>
                                    </v-card-title>
                                </v-flex>
                            </v-layout>
                            <v-divider light></v-divider>
                            <v-card-actions class="pa-3 green--text justify-center">+20 ч : 30 м</v-card-actions>
                        </v-card>
                        <v-card class="kill-card mt-3">
                            <v-layout row justify-center>
                                <v-flex xs12>
                                    <v-card-title class="justify-center">
                                        <div class="headline">Разница
                                            <br>План/Факт
                                        </div>
                                    </v-card-title>
                                </v-flex>
                            </v-layout>
                            <v-divider light></v-divider>
                            <v-card-actions class="pa-3 green--text justify-center">+20 ч : 30 м</v-card-actions>
                        </v-card>
                        <v-card class="kill-card mt-3">
                            <v-layout row justify-center>
                                <v-flex xs12>
                                    <v-card-title class="justify-center">
                                        <div class="headline">Разница
                                            <br>План/Факт
                                        </div>
                                    </v-card-title>
                                </v-flex>
                            </v-layout>
                            <v-divider light></v-divider>
                            <v-card-actions class="pa-3 green--text justify-center">+20 ч : 30 м</v-card-actions>
                        </v-card>
                    </v-flex>
                    <v-flex lg10 xs12>
                        <!--Graphs-->
                        <div class="charts">
                            <div class="chartBox">
                                <div class="chartResults">
                                    <div class="chartResult-item late">
                                        <p>Коэф
                                            <br>опозданий
                                        </p>
                                        <span>0,01%</span>
                                    </div>
                                    <div class="chartResult-item gone">
                                        <p>Коэф
                                            <br>ушел
                                        </p>
                                        <span>0,1%</span>
                                    </div>
                                    <div class="chartResult-item mood">
                                        <p>Коэф
                                            <br>настроение
                                        </p>
                                        <span>72%</span>
                                    </div>
                                </div>
                                <line-chart :chartdata="chartData" :options="chartOptions"/>
                            </div>
                        </div>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
        <v-layout row wrap justify-start align-baseline>
            <v-flex xs2>
                <v-select
                        class="kill-select mt-1"
                        :items="departaments"
                        solo
                        placeholder="Выбор подразделения"
                ></v-select>
            </v-flex>
            <v-flex xs2>
                <v-text-field
                        class="mt-1 normal-border"
                        single-line
                        flat
                        solo
                        label="Поиск"
                        append-icon="search"
                        color="purple"
                ></v-text-field>
            </v-flex>
            <v-flex xs8 justify-start>
                <v-chip label>
                    <span left class="mr-1">13</span>Сотрудников
                </v-chip>
                <v-chip label>
                    <v-icon color="purple">settings</v-icon>
                </v-chip>

                <v-btn class="primary lighten-1 white--text">Отправить ссылку на Face ID</v-btn>
                <v-btn class="primary lighten-1 white--text">Отправить График</v-btn>
            </v-flex>
        </v-layout>
        <v-layout>
            <v-flex xs12>
                <home-table></home-table>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
    import LineChart from "../components/chart/Chart.vue";
    import MyProgress from "../components/progress/Progress";
    import TimeTable from "../components/timeTable/TimeTable";
    import HomeTable from "../components/homeTable/HomeTable";

    export default {
        name: "abn-home",
        head: {
            title() {
                return {
                    inner: "Home"
                };
            }
        },
        components: {
            LineChart,
            MyProgress,
            TimeTable,
            HomeTable
        },
        data: () => ({
            departaments: ["test1", "test2", "test3"],
            value: [200, 675, 410, 390, 310, 460, 250, 240],
            chartData: {
                labels: ["January", "February", "March", "April", "May", "June"],
                datasets: [
                    {
                        label: "Data One",
                        backgroundColor: "#5ae08f",
                        borderColor: "#5ae08f",
                        data: [20, 13, 25, 10, 30, 35],
                        fill: false
                    },
                    {
                        label: "Data Two",
                        backgroundColor: "#fa6d6e",
                        borderColor: "#fa6d6e",
                        data: [35, 28, 40, 25, 45, 45],
                        fill: false
                    },
                    {
                        label: "Data Two",
                        backgroundColor: "#fbbd21",
                        borderColor: "#fbbd21",
                        data: [15, 20, 10, 22, 15, 30],
                        fill: false
                    },
                ]
            },
            chartOptions: {
                steppedLine: false,
                responsive: true,
                scales: {
                    xAxes: [
                        {
                            gridLines: {
                                display: false
                            }
                        }
                    ],
                    yAxes: [
                        {
                            gridLines: {
                                display: false
                            },
                            ticks: {
                                beginAtZero: true,
                                steps: 10,
                                stepValue: 5,
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
            },
            rowsPerPageItems: [4, 8, 12],
            pagination: {
                rowsPerPage: 4
            }
        })
    };
</script>
<style >
    .purpleText {
        color: #7d6df2;
    }

    .main-field {
        background-color: #fff;
        height: 80vh;
        border: #d4d4d4 solid 1px;
        border-radius: 8px;
    }

    .home-wrap {
        padding: 24px 0;
        width: 80%;
    }

    .kill-card {
        width: 100%;
        font-size: 13px;
        border-radius: 5px;
    }

    .kill-card .headline {
        font-size: 13px !important;
        line-height: 16px !important;
    }

    .kill-card * {
        padding: 2px !important;
    }

    .charts {
        display: flex;
        margin-top: 10px;
    }

    .chartBox {
        display: flex;
        width: 100%;
        padding-left: 15px;
    }

    .chartResults {
        display: flex;
        flex-direction: column;
        background-color: #fff;
        justify-content: space-between;
        border: 1px solid #d4d4d4;
        border-radius: 5px;
        box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
        0 1px 5px 0 rgba(0, 0, 0, 0.12);
        font-size: 13px;
    }

    .chartResult-item {
        border-bottom: 1px solid #d4d4d4;
        flex-grow: 1;
    }

    .chartResult-item p {
        border-bottom: 1px solid #d4d4d4;
        margin: 0;
        padding: 2px;
        font-weight: 600;
    }

    .chartResult-item span {
        color: #a3a3a3;
    }

    .late p {
        color: #fa6d6e;
    }

    .gone p {
        color: #f6a944;
    }

    .mood p {
        color: #5ae08f;
    }

    .hideAnalitics {
        text-transform: none;
        color: #fff;
        background-color: #fa6d6e;
        margin-left: 0;
    }
</style>