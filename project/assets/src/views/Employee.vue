<template>
    <v-container grid-list-xl text-xs-center fluid class="home-wrap">
        <v-layout row wrap align-start>
            <v-flex lg4>
                <v-layout row wrap>
                    <v-flex lg12>
                        <div class="employeeFaceId materialBox">
                            <v-layout>
                                <v-flex xs6>
                                    <v-avatar
                                            :size="150"
                                            color="grey lighten-4"
                                    >
                                        <img src="https://vuetifyjs.com/apple-touch-icon-180x180.png" alt="avatar">
                                    </v-avatar>
                                    <v-btn color="get-danger" dark class="removeID">Удалить Face ID</v-btn>
                                </v-flex>
                                <v-flex xs6>
                                    <v-layout align-center justify-space-around column fill-height>
                                        <v-flex>
                                            <v-select
                                                    :items="duties"
                                                    label="Должность"
                                                    solo
                                                    v-model="duty"
                                            >
                                                <template slot="append">
                                                    <v-icon color="purple">fas fa-chevron-circle-right</v-icon>
                                                </template>
                                            </v-select>
                                        </v-flex>
                                        <v-flex>
                                            <v-btn large color="primary" class="white--text">Отправить <br> логин и
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
                        <div class="employeeFaceId materialBox get-orange">
                            <v-flex d-flex row xs12 shrink>
                                <v-layout row wrap>
                                    <v-flex shrink>
                                        <v-card class="card-parent">
                                            <v-card class="get-orange">
                                                <v-card-title>
                                                    Luul
                                                </v-card-title>
                                            </v-card>
                                            <v-card-title>
                                                Hello
                                            </v-card-title>
                                        </v-card>
                                    </v-flex>
                                    <v-flex shrink>
                                        <v-card class="card-parent">
                                            <v-card class="get-orange">
                                                <v-card-title>
                                                    Luul
                                                </v-card-title>
                                            </v-card>
                                            <v-card-title>
                                                Hello
                                            </v-card-title>
                                        </v-card>
                                    </v-flex>
                                    <v-flex grow d-flex>
                                        <div class="add_square__wrap">
                                            <div class="add_square__icon">
                                                <v-icon>add_circle</v-icon>
                                            </div>
                                        </div>
                                    </v-flex>
                                    <v-flex grow d-flex>
                                        <div class="add_square__wrap">
                                            <div class="add_square__icon">
                                                <v-icon>add_circle</v-icon>
                                            </div>
                                        </div>
                                    </v-flex>
                                    <v-flex grow d-flex>
                                        <div class="add_square__wrap">
                                            <div class="add_square__icon">
                                                <v-icon>add_circle</v-icon>
                                            </div>
                                        </div>
                                    </v-flex>
                                </v-layout>
                            </v-flex>
                        </div>
                    </v-flex>
                    <v-flex lg12>
                        <div class="employeeFaceId materialBox">
                            <v-flex d-flex row xs12>
                                <v-layout row wrap>
                                    <v-flex>
                                        <div class="achievent-badge">
                                           <span class="achievent-content">
                                               <img class="achievent-img"
                                                    src="https://stickeroid.com/uploads/pic/full-tlgrm/2bacfa210665b0415873f7cd5c2bbaa1e1b48c64.png"
                                                    alt="">
                                           </span>
                                        </div>
                                    </v-flex>
                                    <v-flex>
                                        <div class="achievent-badge">
                                           <span class="achievent-content">
                                               <img class="achievent-img"
                                                    src="https://stickeroid.com/uploads/pic/full-tlgrm/2bacfa210665b0415873f7cd5c2bbaa1e1b48c64.png"
                                                    alt="">
                                           </span>
                                        </div>
                                    </v-flex>
                                    <v-flex>
                                        <div class="achievent-badge">
                                           <span class="achievent-content">
                                               <img class="achievent-img"
                                                    src="https://stickeroid.com/uploads/pic/full-tlgrm/2bacfa210665b0415873f7cd5c2bbaa1e1b48c64.png"
                                                    alt="">
                                           </span>
                                        </div>
                                    </v-flex>
                                    <v-flex>
                                        <div class="achievent-badge">
                                           <span class="achievent-content">
                                               <img class="achievent-img"
                                                    src="https://stickeroid.com/uploads/pic/full-tlgrm/2bacfa210665b0415873f7cd5c2bbaa1e1b48c64.png"
                                                    alt="">
                                           </span>
                                        </div>
                                    </v-flex>
                                    <v-flex>
                                        <div class="achievent-badge">
                                           <span class="achievent-content">
                                               <img class="achievent-img"
                                                    src="https://stickeroid.com/uploads/pic/full-tlgrm/2bacfa210665b0415873f7cd5c2bbaa1e1b48c64.png"
                                                    alt="">
                                           </span>
                                        </div>
                                    </v-flex>
                                </v-layout>
                            </v-flex>
                        </div>
                    </v-flex>
                </v-layout>
                <div class="fireEmployee"></div>
                <div class="rewards"></div>
            </v-flex>
            <v-flex lg8>
                <v-layout row wrap>
                    <v-flex lg8>
                        <v-layout row wrap>
                            <v-flex lg12>
                                <v-layout row wrap>
                                    <v-flex lg6>
                                        <v-text-field class="input-shadow"
                                                      background-color="white"
                                                      color="purple"
                                                      box label="Имя"
                                        ></v-text-field>
                                        <v-text-field class="input-shadow"
                                                      background-color="white"
                                                      color="purple"
                                                      box label="Фамилия"
                                        ></v-text-field>
                                        <v-text-field class="input-shadow"
                                                      background-color="white"
                                                      color="purple"
                                                      box label="Отчество"
                                        ></v-text-field>
                                        <v-select
                                                :items="duties"
                                                label="Должность"
                                                solo
                                                v-model="duty"
                                        >
                                            <template slot="append">
                                                <v-icon color="purple">fas fa-chevron-circle-right</v-icon>
                                            </template>
                                        </v-select>
                                        <v-select
                                                :items="duties"
                                                label="Подразделение"
                                                solo
                                                v-model="duty"
                                        >
                                            <template slot="append">
                                                <v-icon class="purple--text">fas fa-chevron-down</v-icon>
                                            </template>
                                        </v-select>
                                        <v-text-field class="input-shadow"
                                                      background-color="white"
                                                      color="purple"
                                                      type="tel"
                                                      prefix="+"
                                                      mask="# (###) ###-##-##"
                                                      placeholder="7 (999) 999-99-99"
                                                      box label="Телефон"
                                        ></v-text-field>
                                        <v-text-field class="input-shadow"
                                                      background-color="white"
                                                      color="purple"
                                                      type="email"
                                                      placeholder="infor@example.com"
                                                      box label="Email"
                                        ></v-text-field>

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
                                                <v-btn flat color="purple"
                                                       @click="$refs.datePicker.save(date)"
                                                >OK
                                                </v-btn>
                                            </v-date-picker>
                                        </v-menu>

                                        <v-radio-group
                                                v-model="gender"
                                                row="true"
                                        >
                                            <v-radio
                                                    label="Мужчина"
                                                    value="man"
                                            ></v-radio>
                                            <v-radio
                                                    label="Женщина"
                                                    value="woman"
                                            >
                                            </v-radio>
                                        </v-radio-group>

                                    </v-flex>
                                    <v-flex lg6>
                                        <v-btn large color="get-orange" class="white--text">
                                            <v-icon class="mr-2">edit</v-icon>
                                            Редактировать
                                        </v-btn>
                                    </v-flex>
                                </v-layout>
                            </v-flex>

                            <v-flex lg12 d-flex>
                                <v-layout row wrap>
                                    <v-flex lg6 offset-lg6 xs12>
                                        <v-flex lg12 d-flex grid-list-md>
                                            <v-layout row wrap>
                                                <v-flex xs4>
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
                                                        <v-card-actions class="pa-3 green--text justify-center">
                                                            +20 ч :
                                                            30 м
                                                        </v-card-actions>
                                                    </v-card>
                                                </v-flex>
                                                <v-flex xs4>
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
                                                        <v-card-actions class="pa-3 green--text justify-center">
                                                            +20 ч :
                                                            30 м
                                                        </v-card-actions>
                                                    </v-card>
                                                </v-flex>
                                                <v-flex xs4>
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
                                                        <v-card-actions class="pa-3 green--text justify-center">
                                                            +20 ч :
                                                            30 м
                                                        </v-card-actions>
                                                    </v-card>
                                                </v-flex>
                                            </v-layout>
                                        </v-flex>
                                    </v-flex>
                                </v-layout>
                            </v-flex>
                            <v-flex lg12>
                                <Progress></Progress>
                            </v-flex>
                        </v-layout>
                    </v-flex>
                    <v-flex lg4>
                        <v-btn large color="primary">
                            <v-icon class="mr-2">add_circle</v-icon>
                            Добавить сотрудника
                        </v-btn>
                        <v-btn large outline>Уволенные сотрудники</v-btn>

                        <chart :chartdata="chartData" :options="chartOptions"></chart>
                        <chart :chartdata="chartData" :options="chartOptions"></chart>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import Progress from '../components/progress/Progress'
    import Chart from '../components/chart/Chart'


    export default {
        name: 'Employee',
        components: {
            Progress,
            Chart,
        },
        data() {
            return {
                gender: 'man',
                datePicker: false,
                date: new Date().toISOString().substr(0, 10),
                duties: [
                    'Первая должность',
                    'Вторая',
                    'Третья'
                ],
                duty: 'Первая должность',
                chartData: {
                    labels: ["January", "February", "March", "April", "May", "June"],
                    datasets: [
                        {
                            label: "Data One",
                            backgroundColor: "#5ae08f",
                            borderColor: "#5ae08f",
                            lineTension: 0,
                            data: [0, 13, 10, 30, 12, 6],
                            fill: false,
                        },
                        {
                            label: "Data Two",
                            backgroundColor: "#fa6d6e",
                            borderColor: "#fa6d6e",
                            lineTension: 0,
                            data: [0, 12, 7, 31, 24, 15],
                            fill: false,
                        },
                        {
                            label: "Data Tree",
                            backgroundColor: "#f6a944",
                            borderColor: "#f6a944",
                            lineTension: 0,
                            data: [0, 12, 15, 20, 24, 27],
                            fill: false,
                        }
                    ]
                },
                chartOptions: {
                    responsive: true,
                    steppedLine: false,
                    scales: {
                        xAxes: [
                            {
                                gridLines: {
                                    display: false,
                                }
                            }
                        ],
                        yAxes: [
                            {
                                gridLines: {
                                    display: false,
                                }
                            }
                        ]
                    },
                    legend: {
                        display: false,
                    },
                    tooltips: {
                        cornerRadius: 2,
                        callbacks: {
                            label: tooltipItem => `${tooltipItem.yLabel}: ${tooltipItem.xLabel}`,
                            title: () => null,
                        }
                    }
                },
            }
        }
    }
</script>

<style scoped>
    .home-wrap {
        padding: 24px 0;
        width: 80%;
    }

    .materialBox {
        background-color: #fff;
        /*border: 1px solid #d4d4d4;*/
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
        background: url('../assets/badge.svg') no-repeat center center;
        background-size: cover;
        max-width: 100px;
    }

    .achievent-content {
        display: flex;
        justify-items: center;
        align-items: center;
        height: 100px;
    }

    .achievent-img {
        max-height: 50px;
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

    .employeeBar button {
        width: 90%;
    }
</style>