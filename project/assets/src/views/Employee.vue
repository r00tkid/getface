<template>
    <v-container grid-list-xl text-xs-center fluid class="home-wrap">
        <v-layout row wrap align-start>
            <v-flex lg4>
                <v-layout row wrap>
                    <v-flex lg12>
                        <div class="employeeFaceId materialBox">
                            <v-layout>
                                <v-flex xs6>
                                    <v-avatar :size="150" color="grey lighten-4">
                                        <img src="https://vuetifyjs.com/apple-touch-icon-180x180.png" alt="avatar">
                                    </v-avatar>
                                    <v-btn color="get-danger" dark class="removeID">Удалить Face ID</v-btn>
                                </v-flex>
                                <v-flex xs6>
                                    <v-layout align-center justify-space-around column fill-height>
                                        <v-flex>
                                            <v-select label="Solo field" solo></v-select>
                                        </v-flex>
                                        <v-flex>
                                            <v-btn large color="primary" class="white--text">
                                                Отправить
                                                <br>логин и
                                                пароль
                                            </v-btn>
                                        </v-flex>
                                    </v-layout>
                                </v-flex>
                            </v-layout>
                        </div>
                    </v-flex>
                    <v-flex lg12>
                        <div class="employeeFaceId materialBox">
                            <v-flex d-flex row align-baseline>
                                <v-text-field
                                        class="mt-1 normal-border get-danger--text"
                                        single-line
                                        flat
                                        solo
                                        hide-details
                                        label="Указать причину увольнения"
                                        append-icon="add_circle"
                                        color="get-danger"
                                ></v-text-field>
                                <v-btn large color="get-danger" class="white--text">Уволить</v-btn>
                            </v-flex>
                        </div>
                    </v-flex>
                    <v-flex lg12>
                        <orange-box></orange-box>
                    </v-flex>
                    <v-flex lg12>
                        <employee-awards></employee-awards>
                    </v-flex>
                </v-layout>
            </v-flex>
            <v-flex lg8>
                <v-layout row wrap>
                    <v-flex lg6>
                        <v-layout row wrap>
                            <v-flex lg12>
                                <v-layout row wrap>
                                    <v-flex class="empoloyeeForms" lg12>
                                        <v-text-field
                                                class="input-shadow"
                                                background-color="white"
                                                color="purple"
                                                solo
                                                label="Имя"
                                                outline
                                                hide-details
                                        ></v-text-field>
                                        <v-text-field
                                                class="input-shadow"
                                                background-color="white"
                                                color="purple"
                                                solo
                                                label="Фамилия"
                                                hide-details
                                        ></v-text-field>
                                        <v-text-field
                                                class="input-shadow"
                                                background-color="white"
                                                color="purple"
                                                solo
                                                label="Отчество"
                                                hide-details
                                        ></v-text-field>
                                        <v-select :items="duties" label="Должность" solo v-model="duty" hide-details>
                                            <template slot="append">
                                                <v-icon color="purple">fas fa-chevron-circle-right</v-icon>
                                            </template>
                                        </v-select>
                                        <v-select
                                                :items="duties"
                                                label="Подразделение"
                                                solo
                                                v-model="duty"
                                                hide-details
                                        >
                                            <template slot="append">
                                                <v-icon class="purple--text">fas fa-chevron-down</v-icon>
                                            </template>
                                        </v-select>
                                        <v-text-field
                                                class="input-shadow"
                                                background-color="white"
                                                color="purple"
                                                type="tel"
                                                prefix="+"
                                                mask="# (###) ###-##-##"
                                                placeholder="7 (999) 999-99-99"
                                                solo
                                                label="Телефон"
                                                hide-details
                                        ></v-text-field>
                                        <v-text-field
                                                class="input-shadow"
                                                background-color="white"
                                                color="purple"
                                                type="email"
                                                placeholder="infor@example.com"
                                                solo
                                                label="Email"
                                                hide-details
                                        ></v-text-field>

                                        <v-layout>
                                            <v-flex xs5>
                                                <v-menu
                                                        ref="datePicker"
                                                        :close-on-content-click="false"
                                                        v-model="datePicker"
                                                        full-width
                                                        color="purple"
                                                        :nudge-right="40"
                                                        offset-y
                                                        :return-value.sync="date"
                                                        lazy
                                                        min-width="290px"
                                                        transition="scale-transition"
                                                        hide-details
                                                >
                                                    <v-text-field
                                                            slot="activator"
                                                            v-model="date"
                                                            class="input-shadow"
                                                            background-color="white"
                                                            color="purple"
                                                            solo
                                                            hide-details
                                                            prepend-inner-icon="event"
                                                            readonly
                                                    ></v-text-field>
                                                    <v-date-picker
                                                            v-model="date"
                                                            no-title
                                                            scrollable
                                                            color="primary"
                                                            header-color="red"
                                                    >
                                                        <v-spacer></v-spacer>
                                                        <v-btn flat color="purple" @click="datePicker = false">Cancel
                                                        </v-btn>
                                                        <v-btn flat color="purple" @click="$refs.datePicker.save(date)">
                                                            OK
                                                        </v-btn>
                                                    </v-date-picker>
                                                </v-menu>
                                            </v-flex>
                                            <v-flex xs7>
                                                <v-radio-group v-model="gender" row>
                                                    <v-radio label="Мужчина" value="man"></v-radio>
                                                    <v-radio label="Женщина" value="woman"></v-radio>
                                                </v-radio-group>
                                            </v-flex>
                                        </v-layout>
                                    </v-flex>
                                </v-layout>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                    <v-flex lg6>
                        <v-btn dark color="get-orange">
                            <v-icon class="mr-2">create</v-icon>
                            Редактировать
                        </v-btn>
                        <v-btn color="primary">
                            <v-icon class="mr-2">add_circle</v-icon>
                            Добавить сотрудника
                        </v-btn>
                        <v-btn outline>Уволенные сотрудники</v-btn>
                        <v-btn outline>История изменений</v-btn>
                        <v-layout>
                            <v-flex lg4>
                                <div class="employeeStat-left">
                                    <div class="employeeStat_item">
                                        <div class="statSubTitle">Смен</div>
                                        <div class="statVal">9/10</div>
                                    </div>
                                    <div class="employeeStat_item">
                                        <div class="statSubTitle">Разница</div>
                                        <div class="statVal">-90ч:00м</div>
                                    </div>
                                    <div class="employeeStat_item">
                                        <div class="statSubTitle">Факт</div>
                                        <div class="statVal">90ч:00м</div>
                                    </div>
                                    <div class="employeeStat_item">
                                        <div class="statSubTitle">План</div>
                                        <div class="statVal">90ч:00м</div>
                                    </div>
                                </div>
                            </v-flex>
                            <v-flex lg8>
                                <div class="employeeStat-right">
                                    <div class="chartContainer chartSmall">
                                        <div class="chartPeriod">Кол-во нарушений 6 месяцев</div>
                                        <chart :chartdata="chartData2" :options="chartOptions"></chart>
                                    </div>
                                    <v-layout>
                                        <v-flex xs12>
                                            <h3>В тек. Месяце</h3>
                                            <div class="employeeStat_item">
                                                <div class="statSubTitle">Опоздал</div>
                                                <div class="statVal">3</div>
                                            </div>
                                            <div class="employeeStat_item">
                                                <div class="statSubTitle">Ушел раньше</div>
                                                <div class="statVal">0</div>
                                            </div>
                                        </v-flex>
                                        <v-flex xs12>
                                            <h3>Итого</h3>
                                            <div class="employeeStat_item">
                                                <div class="statSubTitle">Опоздал</div>
                                                <div class="statVal">12</div>
                                            </div>
                                            <div class="employeeStat_item">
                                                <div class="statSubTitle">Ушел раньше</div>
                                                <div class="statVal">5</div>
                                            </div>
                                        </v-flex>
                                    </v-layout>
                                </div>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                    <v-flex lg12>
                        <v-layout class="">
                            <v-flex lg3>
                                <div class="employeeCondition">
                                    <div class="employeeCondition-item">
                                        <div class="conditionText">Вероятность
                                            <br>увольнения
                                        </div>
                                        <div class="emotion">
                                            <span class="emotionIcon">😠</span>
                                            <span>90%</span>
                                        </div>
                                    </div>
                                    <div class="employeeCondition-item">
                                        <div class="conditionText">Настроение</div>
                                        <div class="emotion">
                                            <span class="emotionIcon">😃</span>
                                            <span>90%</span>
                                        </div>
                                    </div>
                                    <div class="employeeCondition-item">
                                        <div class="conditionText">Усталость</div>
                                        <div class="emotion">
                                            <span class="emotionIcon">😓</span>
                                            <span>90%</span>
                                        </div>
                                    </div>
                                </div>
                            </v-flex>
                            <v-flex lg9>
                                <div class="chartContainer chartBottom">
                                    <div class="chartPeriod">Последние 3 месяца</div>
                                    <chart :chartdata="chartData" :options="chartOptions"></chart>
                                </div>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import Progress from "../components/progress/Progress";
    import Chart from "../components/chart/Chart";
    import OrangeBox from "../components/employeePage/OrangeBox";
    import EmployeeAwards from "../components/employeePage/EmployeeAwards";

    export default {
        name: "Employee",
        components: {
            Progress,
            Chart,
            OrangeBox,
            EmployeeAwards
        },
        data() {
            return {
                gender: "man",
                datePicker: false,
                date: new Date().toISOString().substr(0, 10),
                duties: ["Первая должность", "Вторая", "Третья"],
                duty: "Первая должность",
                chartData: {
                    datasets: [
                        {
                            label: "Data One",
                            backgroundColor: "#5ae08f",
                            borderColor: "#5ae08f",
                            lineTension: 0,
                            data: [
                                {x: "01/07/2018", y: 25},
                                {x: "01/08/2018", y: 35},
                                {x: "01/09/2018", y: 15},
                                {x: "01/10/2018", y: 20},
                                {x: "01/11/2018", y: 40},
                                {x: "01/12/2018", y: 30}
                            ],
                            fill: false
                        },
                        {
                            label: "Data One",
                            backgroundColor: "#fbbd21",
                            borderColor: "#fbbd21",
                            lineTension: 0,
                            data: [
                                {x: "01/07/2018", y: 10},
                                {x: "01/08/2018", y: 55},
                                {x: "01/09/2018", y: 30},
                                {x: "01/10/2018", y: 20},
                                {x: "01/11/2018", y: 46},
                                {x: "01/12/2018", y: 60}
                            ],
                            fill: false
                        }
                    ]
                },
                chartData2: {
                    datasets: [
                        {
                            label: "Data One",
                            backgroundColor: "rgba(250, 109, 116, 0.3)",
                            borderColor: "#fa6d74",
                            lineTension: 0,
                            data: [
                                {x: "01/07/2018", y: 25},
                                {x: "01/08/2018", y: 35},
                                {x: "01/09/2018", y: 15},
                                {x: "01/10/2018", y: 20},
                                {x: "01/11/2018", y: 40},
                                {x: "01/12/2018", y: 30}
                            ],
                            fill: true
                        }
                    ]
                },
                chartOptions: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        xAxes: [
                            {
                                display: false,
                                type: "time",
                                time: {
                                    unit: "month",
                                    displayFormats: {
                                        quarter: "MMM YYYY"
                                    }
                                }
                            }
                        ],
                        yAxes: [
                            {
                                display: false,
                                gridLines: {
                                    display: false
                                },
                                ticks: {
                                    display: false,
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
                            label: tooltipItem =>
                                `${tooltipItem.yLabel}: ${tooltipItem.xLabel}`,
                            title: () => null
                        }
                    }
                }
            };
        }
    };
</script>

<style scoped>

    .chartPeriod {
        width: 100%;
        text-align: center;
        border-bottom: 1px solid #d4d4d4;
        padding: 10px 0;
        font-weight: bold;
        font-size: 16px;
    }

    .chartSmall .chartPeriod {
        padding: 5px 0;
        font-size: 14px;
    }

    .home-wrap {
        padding: 24px 0;
        width: 80%;
    }

    .materialBox {
        background-color: #fff;
        border: 1px solid #d4d4d4;
        border-radius: 5px;
        box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
        0 1px 5px 0 rgba(0, 0, 0, 0.12);
        padding: 10px;
    }

    .removeID {
        margin-top: -15px;
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

    .card-parent {
        padding: 4px;
    }

    .add_square__wrap {
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid white;
        background: rgba(256, 256, 256, 0.5);
        -webkit-border-radius: 4px;
        -moz-border-radius: 4px;
        border-radius: 4px;
    }

    .achievent-badge {
        display: flex;
        justify-content: center;
        align-items: center;
        background: url("../assets/badge.svg") no-repeat center center;
        background-size: cover;
        max-width: 100px;
    }

    .achievent-content {
        display: flex;
        justify-items: center;
        align-items: center;
        height: 100px;
    }

    .v-input--selection-controls {
        margin-top: 0;
        padding-top: 0;
    }

    .chartResults {
        display: flex;
        background-color: #fff;
        justify-content: space-between;
        border: 1px solid #d4d4d4;
        border-radius: 5px;
        box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
        0 1px 5px 0 rgba(0, 0, 0, 0.12);
        font-size: 13px;
        margin-top: 15px;
    }

    .chartResult-item {
        border-right: 1px solid #d4d4d4;
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

    .employeeCondition {
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-end;
        background-color: #fff;
        border-radius: 4px;
        box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
        0 1px 5px 0 rgba(0, 0, 0, 0.12);
        border: 1px solid #d4d4d4;
    }

    .employeeCondition-item {
        flex: 1;
    }

    .employeeCondition-item:last-child {
        border-top: 1px solid #d4d4d4;
    }

    .employeeCondition-item:first-child {
        border-right: 1px solid #d4d4d4;
    }

    .conditionText {
        border-bottom: 1px solid #d4d4d4;
        height: 50px;
        padding: 0 5px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .emotion {
        display: flex;
        font-size: 18px;
    }

    .emotion span {
        width: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .emotion span:first-child {
        border-right: 1px solid #d4d4d4;
    }

    .emotionIcon {
        font-size: 28px;
    }

    .employeeStat_item {
        margin-bottom: 18px;
        border: 1px solid #d4d4d4;
        border-radius: 4px;
        box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
        0 1px 5px 0 rgba(0, 0, 0, 0.12);
        background-color: #fff;
    }

    .statSubTitle {
        border-bottom: 1px solid #d4d4dd;
    }

    .statVal {
        font-size: 16px;
        font-weight: bold;
        padding: 5px 0;
    }

    @media screen and (max-width: 960px) {
        .achievent-content {
            height: 70px;
        }

        .achievent-badge {
            max-width: 70px;
        }

        .achievent-img {
            max-height: 30px;
        }
    }

    .chartContainer #line-chart {
        height: 140px;
    }

    .chartSmall #line-chart {
        height: 81px;
    }

    .achievent-img {
        max-height: 50px;
    }

    .v-input__slot {
        min-height: 30px !important;
        border-radius: 4px !important;
    }

    .v-input input {
        max-height: 25px !important;
    }

    .v-text-field--box .v-label {
        top: 15px;
        font-weight: 500;
        font-size: 14px;
    }

    .v-select__selections {
        line-height: 32px;
    }

    .empoloyeeForms .v-input {
        margin-bottom: 15px;
    }

    .v-input--selection-controls .v-input__slot {
        border: none !important;
    }

    .v-input--selection-controls .v-label {
        font-size: 13px;
    }

    .v-input--selection-controls .v-radio {
        margin-right: 10px;
    }

    .v-input--selection-controls .accent--text {
        color: #7d6df2 !important;
    }

    .v-menu__activator .v-input__control {
        margin-bottom: 0;
    }

    .v-input--selection-controls .v-input__control {
        margin-bottom: 0;
    }

    .v-menu__activator .v-input__slot {
        height: 47px;
    }

    .employeeStat-right #line-chart {
        height: 250px;
    }

    .chartBottom #line-chart {
        height: 140px;
    }
</style>
