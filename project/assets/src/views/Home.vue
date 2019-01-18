<template>
    <v-container grid-list-md text-xs-center fluid class="home-wrap">
        <v-layout row wrap justify-end>
            <v-flex xs6 d-flex>
                <v-btn outline color="grey">23 янв 2019</v-btn>
                <v-btn outline color="grey">23 фев 2019</v-btn>

                <v-btn large outline color="grey">Сегодня</v-btn>
                <v-btn large outline color="grey">Неделя</v-btn>
                <v-btn large outline color="purple"> Месяц</v-btn>
                <v-btn large outline color="grey">Год</v-btn>
            </v-flex>
        </v-layout>
        <v-layout row wrap justify-start>
            <v-flex xs6>
                <v-data-iterator
                        :items="items"
                        :rows-per-page-items="rowsPerPageItems"
                        :pagination.sync="pagination"
                        content-tag="v-layout"
                        hide-actions
                        row
                        wrap
                >

                    <v-flex
                            slot="item"
                            slot-scope="props"
                            xs12
                            sm6
                            md4
                            lg3
                    >
                        <v-card>
                            <v-card-title class="subheading font-weight-bold">{{ props.item.name }}</v-card-title>
                            <v-card-title>{{ props.item.name }}</v-card-title>

                            <v-divider></v-divider>

                            <v-list dense>
                                <v-list-tile>
                                    <v-list-tile-content>Calories:</v-list-tile-content>
                                    <v-list-tile-content class="align-end">{{ props.item.calories }}
                                    </v-list-tile-content>
                                </v-list-tile>

                                <v-list-tile>
                                    <v-list-tile-content>Fat:</v-list-tile-content>
                                    <v-list-tile-content class="align-end">{{ props.item.fat }}</v-list-tile-content>
                                </v-list-tile>
                            </v-list>
                        </v-card>
                    </v-flex>
                </v-data-iterator>
            </v-flex>
            <v-flex xs6>
                <v-layout>
                    <v-flex xs2>
                        <v-card class="kill-card mt-3" dense>
                            <v-layout row justify-center>
                                <v-flex xs12>
                                    <v-card-title class="justify-center">
                                        <div class="headline ">Разница <br> План/Факт</div>
                                    </v-card-title>
                                </v-flex>
                            </v-layout>
                            <v-divider light></v-divider>
                            <v-card-actions class="pa-3 green--text justify-center">
                                +20 ч : 30 м
                            </v-card-actions>
                        </v-card>
                        <v-card class="kill-card mt-3">
                            <v-layout row justify-center>
                                <v-flex xs12>
                                    <v-card-title class="justify-center">
                                        <div class="headline ">Разница <br> План/Факт</div>
                                    </v-card-title>
                                </v-flex>
                            </v-layout>
                            <v-divider light></v-divider>
                            <v-card-actions class="pa-3 green--text justify-center">
                                +20 ч : 30 м
                            </v-card-actions>
                        </v-card>
                        <v-card class="kill-card mt-3">
                            <v-layout row justify-center>
                                <v-flex xs12>
                                    <v-card-title class="justify-center">
                                        <div class="headline ">Разница <br> План/Факт</div>
                                    </v-card-title>
                                </v-flex>
                            </v-layout>
                            <v-divider light></v-divider>
                            <v-card-actions class="pa-3 green--text justify-center">
                                +20 ч : 30 м
                            </v-card-actions>
                        </v-card>
                    </v-flex>
                    <v-flex xs10>
                        <!--Graphs-->
                        <div class="charts">
                            <div class="chartBox">
                                <line-chart :chartdata="chartData" :options="chartOptions"/>
                                <div class="chartResults">
                                    <div class="chartResult-item late">
                                        <p>Коэф<br> опозданий</p>
                                        <span>0,01%</span>
                                    </div>
                                    <div class="chartResult-item gone">
                                        <p>Коэф<br> ушел</p>
                                        <span>0,1%</span>
                                    </div>
                                    <div class="chartResult-item mood">
                                        <p>Коэф<br> настроение</p>
                                        <span>72%</span>
                                    </div>
                                </div>
                            </div>
                            <div class="chartBox">
                                <line-chart :chartdata="chartData" :options="chartOptions"/>
                                <div class="chartResults">
                                    <div class="chartResult-item late">
                                        <p>Коэф<br> опозданий</p>
                                        <span>0,01%</span>
                                    </div>
                                    <div class="chartResult-item gone">
                                        <p>Коэф<br> ушел</p>
                                        <span>0,1%</span>
                                    </div>
                                    <div class="chartResult-item mood">
                                        <p>Коэф<br> настроение</p>
                                        <span>72%</span>
                                    </div>
                                </div>
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
            <v-flex xs6 justify-start>
                <v-chip label>
                    <span left class="mr-1">13</span>Сотрудников
                </v-chip>
                <v-chip label>
                    <v-icon color="purple">settings</v-icon>
                </v-chip>

                <v-btn color="purple lighten-1 white--text">Отправить ссылку на Face ID</v-btn>
                <v-btn color="purple lighten-1 white--text">Отправить График</v-btn>

            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
    import LineChart from '../components/chart/Chart.vue'
    export default {
        name: "abn-home",
        head: {
            title() {
                return {
                    inner: 'Home',
                }
            },
        },
        components:{
            LineChart
        },
        data: () => ({
            departaments: [
                'test1',
                'test2',
                'test3'
            ],
            value: [
                200,
                675,
                410,
                390,
                310,
                460,
                250,
                240
            ],
            chartData: {
                labels: ['January', 'February', 'March', 'April', 'May', 'June'],
                datasets: [
                    {
                        label: 'Data One',
                        backgroundColor: '#5ae08f',
                        borderColor: "#5ae08f",
                        lineTension: 0, 
                        data: [0,13,10,30,12,6],
                        fill: false
                    },
                    {
                        label: 'Data Two',
                        backgroundColor: '#fa6d6e',
                        borderColor: "#fa6d6e",
                        lineTension: 0, 
                        data: [0,12,7,31,24,15],
                        fill: false
                    },
                    {
                        label: 'Data Tree',
                        backgroundColor: '#f6a944',
                        borderColor: "#f6a944",
                        lineTension: 0, 
                        data: [0,12,15,20,24,27],
                        fill: false
                    }
                ]
            },
            chartOptions: {
                responsive: true,
                steppedLine: false,
                scales: {
                    xAxes: [{
                        gridLines: {
                            display:false
                        }
                    }],
                    yAxes: [{
                        gridLines: {
                            display:false
                        }   
                    }]
                },
                legend: {
                    display: false,
                },
                tooltips: {
                    cornerRadius: 2,
                    callbacks: {
                        label: tooltipItem => `${tooltipItem.yLabel}: ${tooltipItem.xLabel}`, 
                        title: () => null,
                    },
                },

            },
            rowsPerPageItems: [4, 8, 12],
            pagination: {
                rowsPerPage: 4
            },
            items: [
                {
                    value: false,
                    name: 'Frozen Yogurt',
                    calories: 159,
                    fat: 6.0,
                    carbs: 24,
                    protein: 4.0,
                    sodium: 87,
                    calcium: '14%',
                    iron: '1%'
                },
                {
                    value: false,
                    name: 'Ice cream sandwich',
                    calories: 237,
                    fat: 9.0,
                    carbs: 37,
                    protein: 4.3,
                    sodium: 129,
                    calcium: '8%',
                    iron: '1%'
                },]
        }),
    }
</script>
<style scope>
    .main-field {
        background-color: #fff;
        height: 80vh;
        border: #d4d4d4 solid 1px;
        border-radius: 8px;
    }

    .home-wrap {
        width: 80%;
    }
    .kill-card{
        width: 100%;
        font-size: 13px;
        border-radius: 5px;
    }
    .kill-card .headline{
        font-size: 13px !important;
        line-height: 16px !important;
    }
    .kill-card * {
        padding: 2px !important;
    }
    .charts{
        display: flex;
        margin-top: 10px;
    }
    .chartBox{
        max-width: 50%;
        margin-left: 15px;
    }
    #line-chart{
        width: 250px !important;
        height: 200px !important;
    }
    .chartResults{
        display: flex;
        background-color: #fff;
        justify-content: space-between;
        border: 1px solid #d4d4d4;
        border-radius: 5px;
        box-shadow: 0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12);
        font-size: 13px;
    }
    .chartResult-item{
        border-right: 1px solid #d4d4d4;
        flex-grow: 1;
    }
    .chartResult-item p{
        border-bottom: 1px solid #d4d4d4;
        margin: 0;
        padding: 2px;
        font-weight: 600;
    }
    .chartResult-item span{
        color: #a3a3a3;
    }
    .late p{
        color: #fa6d6e;
    }
    .gone p{
        color: #f6a944;
    }
    .mood p{
        color: #5ae08f;
    }
</style>