<template>
    <v-container grid-list-md text-xs-center fluid class="home-wrap">
        <v-layout row wrap justify-end v-show="getAnalytics">
            <v-flex xs12 d-flex>
                <div class="homeDateChange">
                    <v-btn flat small color="purple">
                        <v-icon>navigate_before</v-icon>
                    </v-btn>
                    <div class="homeDateVal">
                        <span>23 янв 2019</span>-
                        <span>23 фев 2019</span>
                    </div>
                    <v-btn flat small color="purple">
                        <v-icon>navigate_next</v-icon>
                    </v-btn>
                </div>
                <v-btn color="white">Сегодня</v-btn>
                <v-btn color="white">Неделя</v-btn>
                <v-btn color="white">Месяц</v-btn>
                <v-btn color="white">Год</v-btn>
                <v-btn color="#fa6d6e" dark class="hideAnalytics" @click="swapAnalytics()">Скрыть аналитику</v-btn>
            </v-flex>
        </v-layout>
        <v-layout row wrap justify-end v-show="!getAnalytics">
            <v-btn color="#fa6d6e" dark class="hideAnalytics" @click="swapAnalytics()">Показать аналитику</v-btn>
        </v-layout>
        <v-layout row wrap justify-start>
            <v-flex lg6 xs12>
                <v-layout row wrap justify-start>
                    <div class="mainChartContainer">
                        <line-chart :enableEvent="false" :series="getLineSeries" :colors="colorsChart"></line-chart>
                    </div>
                </v-layout>
            </v-flex>
            <v-flex lg6 xs12>
                <v-layout>
                    <v-flex lg6 class="mainStat">
                        <home-stat :items="getStat" :colors="colorsChart"></home-stat>
                    </v-flex>
                    <v-flex lg6>
                        <home-time-table></home-time-table>
                    </v-flex>
                </v-layout>

                <get-face-home-analytics></get-face-home-analytics>

                <v-layout row wrap justify-start align-baseline>
                    <v-flex xs2>
                        <v-select
                                class="kill-select mt-1"
                                :items="departments"
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
                            <span left class="mr-1">13</span>&nbsp;Сотрудников
                        </v-chip>
                        <v-chip label>
                            <v-icon color="purple">settings</v-icon>
                        </v-chip>

                        <v-btn class="primary lighten-1 white--text">Отправить ссылку на Face ID</v-btn>
                        <v-btn class="primary lighten-1 white--text">Отправить График</v-btn>
                    </v-flex>
                </v-layout>
                <v-layout>
                    <v-flex xs6 class="pa-0">
                        <home-table></home-table>
                    </v-flex>
                    <v-flex xs6 class="pa-0">
                        <calendar-table></calendar-table>
                    </v-flex>
                </v-layout>
    </v-container>
</template>

<script>
    import {createNamespacedHelpers} from 'vuex';
    import HomeTable from "../components/homeTable/HomeTable";
    import Analytics from "../components/pages/home/Analytics";
    import CalendarTable from "../components/homeTable/CalendarTable";
    import LineChart from "../components/LineChart";
    import HomeTimeTable from "../components/HomeTimeTable";
    import HomeStat from "../components/ToggleStat";

    const {mapState, mapMutations} = createNamespacedHelpers('session/pages/main');

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
            'get-face-home-analytics': Analytics,
            HomeTable,
            CalendarTable,
            LineChart,
            HomeTimeTable,
            HomeStat,
        },
        data: () => ({
            colorsChart: [
                "#38baf5",
                "#f8bc40",
                "#e05116",
                "#6622fd",
                "#f90018",
                "#42f422",
                "#E91E63",
                "#CDDC39"
            ],
            departments: ["test1", "test2", "test3"],
            value: [200, 675, 410, 390, 310, 460, 250, 240],
            rowsPerPageItems: [4, 8, 12],
            pagination: {
                rowsPerPage: 4
            },
        }),
        methods: {
            ...mapMutations([
                'swapAnalytics',
            ]),
        },
        computed: {
            ...mapState({
                getAnalytics: state => state.showAnalytics,
            }),
            getStat() {
                return this.$store.getters.getHomeStat;
            },
            getLineSeries() {
                return this.$store.getters.getSeries;
            }
        },
    };
</script>

<style scoped>
    .home-wrap {
        padding: 24px 0;
        width: 80%;
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
        width: 85%;
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

    .hideAnalytics {
        text-transform: none;
        color: #fff;
        background-color: #fa6d6e;
        margin-left: 0;
    }
</style>