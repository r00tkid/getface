<template>
    <div class="mainChartContainer">
        <v-btn class="addEventBtn" color="white" @click="addEvenShow = !addEvenShow">
            <v-icon class="mr-2" color="purple">list</v-icon>
            Добавить событие
        </v-btn>
        <div v-show="addEvenShow" class="addEvent">
            <div class="addEventHeader">
                <h4>Добавить собитие</h4>
                <v-btn flat icon color="white" @click="addEvenShow = false">
                    <v-icon size="16">close</v-icon>
                </v-btn>
            </div>
            <div class="addEventBody materialBox">
                <v-menu
                        ref="datePicker"
                        :close-on-content-click="false"
                        v-model="datePicker"
                        hint="MM/DD/YYYY format"
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
                    <v-date-picker v-model="date" no-title scrollable color="primary" header-color="red">
                        <v-spacer></v-spacer>
                        <v-btn flat color="purple" @click="datePicker = false">Cancel</v-btn>
                        <v-btn flat color="purple" @click="$refs.datePicker.save(date)">OK</v-btn>
                    </v-date-picker>
                </v-menu>
                <p v-show="areaError" class="eventError">Необходимо заполнить описание события</p>
                <v-textarea solo class="mt-2" name="input-7-4" v-model="textAreaVal" hide-details></v-textarea>
                <v-btn class="ml-0" disable color="white" @click="addAnnotation">Добавить событие</v-btn>
            </div>
        </div>
        <apexchart ref="chart" height="400" type="line" :options="lineOptions" :series="series"></apexchart>
    </div>
</template>
<script>
    export default {
        props: {
            colors: {
                type: Array,
                required: true
            }
        },
        data() {
            return {
                date: new Date().toISOString().substr(0, 10),
                datePicker: false,
                addEvenShow: false,
                textAreaVal: "",
                areaError: false,
                annotID: 0,
                existAnnotations: [],
                lineOptions: {
                    chart: {
                        id: "vuechart-example",
                        toolbar: {
                            show: true,
                            tools: {
                                download: true,
                                selection: true,
                                zoom: true,
                                zoomin: true,
                                zoomout: true
                            }
                        }
                    },
                    colors: this.colors,
                    tooltip: {},
                    xaxis: {
                        type: "datetime",
                        labels: {
                            format: "dd.MM"
                        }
                    },
                    yaxis: {
                        show: true,
                        showAlways: true,
                        max: 100,
                        tickAmount: 5,
                        axisBorder: {
                            show: true
                        }
                    },
                    stroke: {
                        width: 1.5
                    },
                    legend: {
                        show: false
                    },
                    annotations: {
                        xaxis: []
                    }
                },
                series: [
                    {
                        name: "Series 1",
                        data: [
                            {
                                x: "03-17-2019",
                                y: 34
                            },
                            {
                                x: "03-18-2019",
                                y: 43
                            },
                            {
                                x: "03-19-2019",
                                y: 31
                            },
                            {
                                x: "03-20-2019",
                                y: 43
                            },
                            {
                                x: "03-21-2019",
                                y: 33
                            },
                            {
                                x: "03-22-2019",
                                y: 0
                            }
                        ]
                    },
                    {
                        name: "Series 2",
                        data: [
                            {
                                x: "03-17-2019",
                                y: 20
                            },
                            {
                                x: "03-18-2019",
                                y: 35
                            },
                            {
                                x: "03-19-2019",
                                y: 50
                            },
                            {
                                x: "03-20-2019",
                                y: 30
                            },
                            {
                                x: "03-21-2019",
                                y: 60
                            },
                            {
                                x: "03-22-2019",
                                y: 0
                            }
                        ]
                    }
                ]
            };
        },
        methods: {
            addAnnotation() {
                if (this.textAreaVal.length == 0) {
                    this.areaError = true;
                } else {
                    let annotationObj = {
                        id: this.annotID,
                        date: new Date(this.date).toLocaleString("en-US").substr(0, 9)
                    };
                    this.areaError = false;
                    let obj = this.existAnnotations.find(
                        val => val.date == annotationObj.date
                    );
                    if (obj == undefined) {
                        this.existAnnotations.push(annotationObj);
                        this.createAnnotation(annotationObj.date, annotationObj.id);
                        this.createChartModal(
                            annotationObj.id,
                            annotationObj.date,
                            this.textAreaVal
                        );
                        this.annotID++;
                    } else {
                        this.updateAnnotation(obj.id, this.textAreaVal);
                    }
                }
            },
            updateAnnotation(id, text) {
                let modal = document.querySelector(`.chartModal${id}`);
                let li = document.createElement("LI");
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
                let modal = document.querySelector(`.chartModal${id}`);

                if (!modal) {
                    let chartModal = document.createElement("div");

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

                    document.querySelector(`.modalChartClose${id}`)
                        .addEventListener("click", e => {
                            chartModal.setAttribute("style", `display: none;`);
                        });
                } else {
                    let list = modal.querySelector(".modalChartList");

                    if (list) {
                        let part = document.createElement("li");
                        part.innerText = text;

                        list.appendChild(part);
                    }
                }
            }
        }
    };
</script>

<style>
    .addEventBtn {
        position: absolute;
        top: 27px;
        left: 50px;
        z-index: 99;
        border: 1px solid #000;
        color: #969696;
    }

    .addEvent {
        position: absolute;
        width: 400px;
        top: 71px;
        left: 57px;
        z-index: 99;
    }

    .addEventHeader {
        background: linear-gradient(
                to right top,
                #7d6df2,
                #9077f4,
                #a181f6,
                #b08bf9,
                #be96fb
        );
        color: #fff;
        padding: 5px;
        border-radius: 4px 4px 0 0;
        display: flex;
        justify-content: space-between;
        align-content: center;
    }

    .addEventHeader button {
        width: 20px;
        height: 20px;
        margin: 0;
    }

    .addEventBody {
        border-radius: 0 0 4px 4px;
    }

    .addEvent .v-menu {
        width: 150px;
    }

    .addEvent .v-input {
        font-size: 13px !important;
    }

    .eventError {
        position: absolute;
        right: 10px;
        top: 70px;
        font-size: 10px;
        color: red;
    }

    .chartModal {
        display: none;
        background: #fff;
        min-width: 200px;
        padding: 0;
        border: 1px solid #ccc;
        position: absolute;
        top: 0;
        left: 0;
        border-radius: 4px;
        z-index: 99999;
    }

    .modalChartClose {
        position: absolute;
        top: 3px;
        right: 5px;
        color: #fff;
        font-size: 16px;
        cursor: pointer;
    }

    .chartModal h4 {
        color: #fff;
        background: linear-gradient(
                to right top,
                #7d6df2,
                #9077f4,
                #a181f6,
                #b08bf9,
                #be96fb
        );
        padding: 5px 15px;
    }

    .chartModal ul {
        padding: 10px 10px 10px 25px;
        list-style: none;
    }

    .chartModal ul li {
        position: relative;
    }

    .chartModal ul li:before {
        position: absolute;
        content: "☷";
        top: 2px;
        left: -15px;
        font-size: 10px;
        color: #7d6df2;
    }
</style>