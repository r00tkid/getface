<template>
    <v-container grid-list-md text-xs-center fluid class="home-wrap">
        <v-layout row wrap justify-end>
            <v-flex xs12 d-flex>
                <v-btn outline color="grey">23 янв 2019</v-btn>
                <v-btn outline color="grey">23 фев 2019</v-btn>
                <v-btn outline color="grey">Сегодня</v-btn>
                <v-btn outline color="grey">Неделя</v-btn>
                <v-btn outline color="purple">Месяц</v-btn>
                <v-btn outline color="grey">Год</v-btn>
                <v-btn color="#fa6d6e" dark class="hideAnalitics">Скрыть аналитику</v-btn>
            </v-flex>
        </v-layout>
        <v-layout row wrap justify-start>
            <v-flex lg6 xs12>
                <v-layout row wrap justify-start>
                    <div class="mainChartContainer">
                        <line-chart :chartdata="chartData" :options="chartOptions"/>
                    </div>
                </v-layout>
            </v-flex>
            <v-flex lg6 xs12>
                <v-layout>
                    <v-flex lg6 class="mainStat">
                        <div class="mainStat-row">
                            <div class="statCheckbox mainStatCommon">
                                <input type="checkbox" name="violation" id="violation">
                            </div>
                            <div class="statLabel mainStatCommon">
                                <label for="violation">Нарушений</label>
                            </div>
                            <div class="statTotal mainStatCommon">
                                45
                            </div>
                        </div>
                        <div class="mainStat-row">
                            <div class="statCheckbox mainStatCommon">
                                <input type="checkbox" name="lateness" id="lateness">
                            </div>
                            <div class="statLabel mainStatCommon">
                                <label for="lateness">Опозданий</label>
                            </div>
                            <div class="statTotal mainStatCommon">
                                45
                            </div>
                        </div>
                        <div class="mainStat-row">
                            <div class="statCheckbox mainStatCommon">
                                <input type="checkbox" name="leftEarlier" id="leftEarlier">
                            </div>
                            <div class="statLabel mainStatCommon">
                                <label for="leftEarlier">Ушёл раньше</label>
                            </div>
                            <div class="statTotal mainStatCommon">
                                45
                            </div>
                        </div>
                        <div class="mainStat-row">
                            <div class="statCheckbox mainStatCommon">
                                <input type="checkbox" name="timeDiference" id="timeDiference">
                            </div>
                            <div class="statLabel mainStatCommon">
                                <label for="timeDiference">Разница часов</label>
                            </div>
                            <div class="statTotal mainStatCommon">
                                45
                            </div>
                        </div>
                        <div class="mainStat-row">
                            <div class="statCheckbox mainStatCommon">
                                <input type="checkbox" name="factTime" id="factTime">
                            </div>
                            <div class="statLabel mainStatCommon">
                                <label for="factTime">Факт часов</label>
                            </div>
                            <div class="statTotal mainStatCommon">
                                45
                            </div>
                        </div>
                        <div class="mainStat-row">
                            <div class="statCheckbox mainStatCommon">
                                <input type="checkbox" name="planTime" id="planTime">
                            </div>
                            <div class="statLabel mainStatCommon">
                                <label for="planTime">План часов</label>
                            </div>
                            <div class="statTotal mainStatCommon">
                                45
                            </div>
                        </div>
                        <div class="mainStat-row">
                            <div class="statCheckbox mainStatCommon">
                                <input type="checkbox" name="statMood" id="statMood">
                            </div>
                            <div class="statLabel mainStatCommon">
                                <label for="statMood">Настроение</label>
                            </div>
                            <div class="statTotal mainStatCommon">
                                45
                            </div>
                        </div>
                        <div class="mainStat-row">
                            <div class="statCheckbox mainStatCommon">
                                <input type="checkbox" name="fatigue" id="fatigue">
                            </div>
                            <div class="statLabel mainStatCommon">
                                <label for="fatigue">Усталость</label>
                            </div>
                            <div class="statTotal mainStatCommon">
                                45
                            </div>
                        </div>
                    </v-flex>
                    <v-flex lg6></v-flex>
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
                                parser: "DD/MM/YYYY", // Pay attention to f***ing warnings
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
            },
            rowsPerPageItems: [4, 8, 12],
            pagination: {
                rowsPerPage: 4
            }
        })
    };
</script>

<style scoped>
    .chartContainer {
        position: relative;
        width: 100%;
        border: 1px solid #d4d4d4;
        border-radius: 4px 4px 0 0;
        box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
        0 1px 5px 0 rgba(0, 0, 0, 0.12);
    }

    .mainChartContainer {
        width: 100%;
    }

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

    .mainStat-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .statCheckbox {
        flex: 1;
    }

    .statLabel {
        flex: 3;
    }

    .statLabel label {
        padding: 10px;
        cursor: pointer;
    }

    .statTotal {
        flex: 2;
    }

    .mainStatCommon {
        margin: 1px;
        padding: 12px 0;
        background-color: #fff;
        border-radius: 3px;
        border: 1px solid #d4d4d4;
    }

    .mainStat-row input[type="checkbox"] {
        opacity: 0;
        z-index: -1;
    }

    input[type="checkbox"]:checked + label,
    input[type="checkbox"]:not(:checked) + label, {
        position: relative;
        width: 120px;
    }

    input[type="checkbox"]:checked + label:before,
    input[type="checkbox"]:not(:checked) + label:before, {
        position: absolute;
        content: '';
        width: 18px;
        height: 18px;
        left: -50px;
        top: 0;
        border: 1px solid #dddddd;
        background-color: #ffffff;
    }
</style>