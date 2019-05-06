<template>
    <v-container class="analiticsContainer" fluid>
        <v-layout>
            <v-flex xs12 d-flex align-self-center>
                <div class="homeDateChage">
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
                <v-btn color="white">3 месяца</v-btn>
                <v-btn color="white">Все</v-btn>
                <div class="groupBtn">
                    <span>Групировать</span>
                    <v-select :items="groupBy" label="Solo field" solo hide-details></v-select>
                </div>
            </v-flex>
        </v-layout>
        <v-layout class="mt-2">
            <v-flex class="materialBox mr-2" xs4>
                <h4>Портрет нашего клиента (Рейтинг)</h4>
                <p class="mb-1">
                    Всего человек:
                    <span>150</span>
                </p>
                <span class="devider"></span>
                <keep-alive>
                    <analitic-slider></analitic-slider>
                </keep-alive>
            </v-flex>
            <v-flex class="materialBox mr-2" xs3>
                <h4>Возраст клиентов</h4>
                <p class="mb-1">
                    Средний возраст:
                    <span>35лет</span>
                </p>
                <span class="devider"></span>
                <p class="smallGreyText">Среднее время присутствия</p>
                <chart-bar :chartdata="chartData" :options="options"/>
            </v-flex>
            <v-flex class="materialBox" xs5>
                <v-layout class="pl-2 pr-2">
                    <v-flex xs8>
                        <h4>Количество клиентов по времени</h4>
                        <p class="mb-1">
                            Среднее количество:
                            <span>450 чел.</span>
                        </p>
                    </v-flex>
                    <v-flex xs4>
                        <v-select :items="groupBy" label="Solo field" solo hide-details></v-select>
                    </v-flex>
                </v-layout>
                <span class="devider"></span>
                <p class="smallGreyText">Количество пользователей по времени суток</p>
                <heat-map></heat-map>
            </v-flex>
        </v-layout>
        <v-layout>
            <v-flex class="materialBox mt-2" xs12>
                <v-layout v-if="tags.length" align-center justify-start row>
                    <template v-for="(tag,i) in tags">
                        <div class="statCheckbox statCommon" :key="i">
                            <input type="checkbox" v-model="tag.selected" name="camera1" :id="`camera${i}`">
                            <label :for="`camera${i}`">{{ tag.name }}</label>
                        </div>
                    </template>
                </v-layout>

                <v-layout>
                    <v-flex class="mt-2" xs9>
                        <analitic-line-chart :series="getLineSeries" :enableEvent="true" :colors="colorsChart"></analitic-line-chart>
                    </v-flex>
                    <v-flex class="mt-3 ml-2" xs3>
                        <analitic-stat :items="getStat" @toggleseries="toggleSeries($event)" :colors="colorsChart"></analitic-stat>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
        <v-layout>
            <v-flex class="mt-2" xs12>
                <analitic-table></analitic-table>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import ChartBar from "../components/charts/ChartBar";
    import HeatMap from "../components/analitics/HeatMap";
    import AnaliticStat from "../components/ToggleStat";
    import AnaliticTable from "../components/analitics/AnaliticTable";
    import AnaliticLineChart from "../components/LineChart";
    import AnaliticSlider from "../components/analitics/AnaliticSlider";

    export default {
        name: "Analitics",
        components: {
            ChartBar,
            HeatMap,
            AnaliticLineChart,
            AnaliticStat,
            AnaliticTable,
            AnaliticSlider
        },
        data() {
            return {
                groupBy: ["Все", "Сегодня", "Неделя", "Месяц", "3 месяца"],
                colorsChart: [
                    "#38baf5",
                    "#f8bc40",
                    "#e05116",
                    "#6622fd",
                    "#f90018",
                    "#42f422"
                ],
                chartData: {
                    datasets: [
                        {
                            label: "Мужчины",
                            data: [10, 20, 30, 5, 20],
                            backgroundColor: "#36d4d4",
                            xAxisID: "xAxis1"
                        },
                        {
                            label: "Женщины",
                            data: [20, 10, 10, 10, 5],
                            backgroundColor: "#e8b667",
                            xAxisID: "xAxis1"
                        }
                    ]
                },
                options: {
                    plugins: {
                        datalabels: {
                            color: "#000",
                            align: "left",
                            font: {
                                size: "10"
                            },
                            anchor: "end",
                            formatter: function (value, context) {
                                let maleVal = context.chart.config.data.datasets[0].data;
                                let femaleVal = context.chart.config.data.datasets[1].data;
                                let index = context.dataIndex;
                                if (context.datasetIndex == 1) {
                                    return maleVal[index] + femaleVal[index] + "%";
                                } else {
                                    return "";
                                }
                            }
                        }
                    },
                    scales: {
                        xAxes: [
                            {
                                stacked: true,
                                id: "xAxis1",
                                type: "category",
                                labels: ["😠", "😊", "😡", "😄", "😄"],
                                gridLines: {
                                    borderDash: ["5", "4"]
                                },
                                barPercentage: 0.4
                            },
                            {
                                id: "xAxis2",
                                stacked: true,
                                labels: ["До 18", "18-24", "24-35", "35-45", "45+"],
                                gridLines: {
                                    display: false,
                                    drawOnChartArea: false,
                                    borderDash: ["5", "4"]
                                },
                                offset: true
                            },
                            {
                                id: "xAxis3",
                                stacked: true,
                                labels: ["1ч:35м", "1ч:35м", "1ч:35м", "1ч:35м", "1ч:35м"],
                                gridLines: {
                                    display: false,
                                    drawOnChartArea: false,
                                    borderDash: ["5", "4"]
                                },
                                position: "top",
                                offset: true
                            }
                        ],
                        yAxes: [
                            {
                                stacked: true,
                                ticks: {
                                    max: 100,
                                    stepSize: 25,
                                    callback: val => {
                                        return val + "%";
                                    }
                                },
                                gridLines: {
                                    borderDash: ["5", "4"]
                                }
                            }
                        ]
                    },
                    tooltips: {
                        enabled: false,
                        custom: function (tooltipModel) {
                            let tooltipEl = document.getElementById("chartjs-tooltip");

                            if (!tooltipEl) {
                                tooltipEl = document.createElement("div");
                                tooltipEl.id = "chartjs-tooltip";
                                document.body.appendChild(tooltipEl);
                            }
                            if (tooltipModel.dataPoints) {
                                let index = tooltipModel.dataPoints[0].index;
                                let maleVal = this._data.datasets[0].data[index];
                                let femaleVal = this._data.datasets[1].data[index];

                                // Tooltip Element

                                // Create element on first render

                                // Hide if no tooltip
                                if (tooltipModel.opacity === 0) {
                                    tooltipEl.style.opacity = 0;
                                    return;
                                }

                                // Set caret Position
                                tooltipEl.classList.remove("above", "below", "no-transform");
                                if (tooltipModel.yAlign) {
                                    tooltipEl.classList.add(tooltipModel.yAlign);
                                } else {
                                    tooltipEl.classList.add("no-transform");
                                }

                                function getBody(bodyItem) {
                                    return bodyItem.lines;
                                }

                                // Set Text
                                if (tooltipModel.body) {
                                    let bodyLines = tooltipModel.body.map(getBody);

                                    let innerHtml = "";

                                    bodyLines.forEach(function (body, i) {
                                        innerHtml += `<div class="tooltipGender tooltipMale"><small>◉</small><p>Мужчины: &nbsp;100чел.</p><span>${maleVal}%</span></div>
                                <div class="tooltipGender tooltipFemale"><small>◉</small><p>Женщины: 100чел.</p><span>${femaleVal}%</span></div>
                                <div class="tooltipCommon">Общее количество: 200чел.</div>`;
                                    });

                                    tooltipEl.innerHTML = innerHtml;
                                }
                                // `this` will be the overall tooltip
                                let position = this._chart.canvas.getBoundingClientRect();

                                // Display, position, and set styles for font
                                tooltipEl.style.opacity = 1;
                                tooltipEl.style.position = "absolute";
                                tooltipEl.style.left =
                                    position.left + window.pageXOffset + tooltipModel.caretX + "px";
                                tooltipEl.style.top =
                                    position.top + window.pageYOffset + tooltipModel.caretY + "px";
                                tooltipEl.style.fontFamily = tooltipModel._bodyFontFamily;
                                tooltipEl.style.fontSize = tooltipModel.bodyFontSize + "px";
                                tooltipEl.style.fontStyle = tooltipModel._bodyFontStyle;
                                tooltipEl.style.padding =
                                    tooltipModel.yPadding + "px " + tooltipModel.xPadding + "px";
                                tooltipEl.style.pointerEvents = "none";
                                tooltipEl.style.background = "#fff";
                                tooltipEl.style.border = "1px solid #ccc";
                                tooltipEl.style.borderRadius = "4px";
                                tooltipEl.style.color = "#969696";
                            } else {
                                tooltipEl.style.opacity = 0;
                            }
                        }
                    },
                    legend: {display: false}
                }
            };
        },
        methods: {
            toggleSeries(e) {
                this.seriesIndex = e;
            },
        },
        computed: {
            tags() {
                let data = this.$store.getters.getAllDataTable;
                let selected = [];
                data.forEach(elem => {
                    if (elem.items == undefined && elem.selected == true) {
                        selected.push(elem);
                    } else if (elem.items) {
                        elem.items.forEach(item => {
                            if (item.selected == true) {
                                selected.push(item);
                            }
                        });
                    }
                });
                return selected;
            },
            getStat() {
                return this.$store.getters.getStat;
            },
            getLineSeries() {
                return this.$store.getters.getLineSeries;
            }
        }
    };
</script>

<style scoped>
    .devider {
        width: 100%;
        height: 1px;
        background-color: #d4d4d4;
        margin: 10px 0;
        display: block;
    }

    .groupBtn {
        display: flex;
        align-items: center;
    }

    .groupBtn span {
        margin-right: 10px;
    }

    .analiticsContainer {
        width: 90%;
    }

    @media only screen and (max-width: 1250px) {
        .analiticsContainer {
            width: 100%;
        }
    }

    /* checkbox styling */

    .statCheckbox {
        position: relative;
    }

    input[type="checkbox"] + label:before {
        border: 2px solid #7d6df2;
        content: "\00a0";
        display: inline-block;
        height: 18px;
        width: 18px;
        margin: 0 0.25em 0 0;
        padding: 0;
        border-radius: 3px;
        vertical-align: top;
        position: absolute;
        left: 9px;
    }

    input[type="checkbox"]:checked + label:before {
        background: linear-gradient(
                to right top,
                #7d6df2,
                #9077f4,
                #a181f6,
                #b08bf9,
                #be96fb
        );
        text-align: center;
    }

    input[type="checkbox"]:checked + label:after {
        font-weight: bold;
        content: "⅃";
        position: absolute;
        transform: rotate(45deg);
        left: 13px;
        top: 4px;
        font-size: 16px;
        color: #fff;
    }

    input[type="checkbox"]:focus + label::before {
        outline: rgb(59, 153, 252) auto 5px;
    }

    .statTotal {
        flex: 2;
    }

    .statCommon {
        background-color: #fff;
        border: 1px solid #d4d4d4;
        height: 35px;
        border-radius: 3px;
        margin-right: 3px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .statCheckbox input[type="checkbox"] {
        visibility: hidden;
    }

    .statCheckbox {
        display: flex;
        align-items: center;
        justify-content: center;
        min-width: 115px;
    }

    .statCheckbox label {
        cursor: pointer;
        font-size: 12px;
    }

    /* checkbox styling */
    .homeDateVal span {
        white-space: nowrap;
    }
</style>