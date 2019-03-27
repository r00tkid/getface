<template>
    <v-container grid-list-md text-xs-center fluid class="home-wrap">
        <v-layout row wrap justify-end v-show="getAnalytics">
            <v-flex xs12 d-flex>
                <div class="homeDateChange">
                    <v-btn flat small color="purple">
                        <v-icon>navigate_before</v-icon>
                    </v-btn>
                    <div class="homeDateVal"><span>23 янв 2019</span>-<span>23 фев 2019</span></div>
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
    import {createNamespacedHelpers} from 'vuex';

    import HomeTable from "../components/homeTable/HomeTable";
    import Analytics from "../components/pages/home/Analytics";

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
        },
        data: () => ({
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
        },
    };
</script>

<style scoped>
    .home-wrap {
        padding: 24px 0;
        width: 80%;
    }

    .hideAnalytics {
        text-transform: none;
        color: #fff;
        background-color: #fa6d6e;
        margin-left: 0;
    }
</style>