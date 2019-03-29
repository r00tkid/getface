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
                <analitic-slider></analitic-slider>
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
                <v-layout>
                    <v-flex xs4 d-flex>
                        <div class="statCheckbox statCommon">
                            <input type="checkbox" name="camera1" id="camera1">
                            <label for="camera1">Камера 1</label>
                        </div>
                        <div class="statCheckbox statCommon">
                            <input type="checkbox" name="camera2" id="camera2">
                            <label for="camera2">Камера 2</label>
                        </div>
                        <div class="statCheckbox statCommon">
                            <input type="checkbox" name="camera3" id="camera3">
                            <label for="camera3">Камера 3</label>
                        </div>
                        <div class="statCheckbox statCommon">
                            <input type="checkbox" name="camera4" id="camera4">
                            <label for="camera4">Камера 4</label>
                        </div>
                    </v-flex>
                </v-layout>
                <v-layout>
                    <v-flex class="mt-2" xs9>
                        <analitic-line-chart :colors="colorsChart"></analitic-line-chart>
                    </v-flex>
                    <v-flex class="mt-3 ml-2" xs3>
                        <analitic-stat :colors="colorsChart"></analitic-stat>
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
    import AnaliticStat from "../components/analitics/AnaliticStat";
    import AnaliticTable from "../components/analitics/AnaliticTable";
    import AnaliticLineChart from "../components/analitics/AnaliticLineChart";
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
                colorsChart: ['#38baf5', '#f8bc40', '#e05116', '#6622fd', '#f90018', '#42f422'],
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
                        callbacks: {
                            label: function (tooltipItem, data) {
                                var label = data.datasets[tooltipItem.datasetIndex].label || "";
                                return `${label}: ${tooltipItem.yLabel}%`;
                            }
                        }
                    },
                    legend: {display: false}
                },
            };
        },
        methods: {
            addAnnotation() {
                if (this.textAreaVal.length == 0) {
                    this.areaError = true;
                } else {
                    let annotationObj = {
                        id: this.annotID,
                        date: new Date(this.date).toLocaleString("en-US").substr(0, 9),
                    };

                    this.areaError = false;

                    let obj = this.existAnnotations.find(val => val.date == annotationObj.date);

                    if (obj == undefined) {
                        this.existAnnotations.push(annotationObj);
                        this.createAnnotation(annotationObj.date, annotationObj.id);
                        this.createChartModal(annotationObj.id, annotationObj.date, this.textAreaVal);
                        this.annotID++;
                    } else {
                        this.updateAnnotation(obj.id, this.textAreaVal);
                    }

                }
            },
            updateAnnotation(id, text) {
                let modal = document.querySelector(`.chartModal${id}`);
                let li = document.createElement('LI');
                li.innerText = text;
                modal.childNodes[3].appendChild(li);
            },
            createAnnotation(date, id) {
                this.$refs.chart.addXaxisAnnotation({
                    x: new Date(date).getTime(),
                    strokeDashArray: 0,
                    borderColor: "#775DD0",
                    label: {
                        borderColor: "#775DD0",
                        style: {
                            color: "#fff",
                            background: "#775DD0",
                            cssClass: `annot${id}`
                        },
                        orientation: "horizontal",
                        text: "☰"
                    }
                });
            },
            createChartModal(id, date, text) {
                let annot = document.querySelector(`.annot${id}`);
                let chartModal = document.createElement("div");
                let myDate = new Date(date);
                chartModal.classList.add(`chartModal${id}`);
                chartModal.classList.add(`chartModal`);
                chartModal.innerHTML = `
                    <h4 class="modalChartHead">${date}<span class="modalChartClose modalChartClose${id}">✕<span></h4>
                    <ul class="modalChartList">
                        <li>${text}</li>
                    </ul>
                `;
                document.body.appendChild(chartModal);
                annot.addEventListener("click", e => {
                    console.log(e);
                    let x = e.pageX;
                    let y = e.pageY;
                    chartModal.setAttribute(
                        "style",
                        `top: ${y}px; left: ${x}px; display: block;`
                    );
                });
                document
                    .querySelector(`.modalChartClose${id}`)
                    .addEventListener("click", e => {
                        chartModal.setAttribute("style", `display: none;`);
                    });
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
    }

    .statCheckbox label {
        cursor: pointer;
        font-size: 12px;
    }

    /* checkbox styling */
</style>