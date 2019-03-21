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
        <v-layout class="ourClientSlider">
          <v-flex xs4 class="ourClientSlider-item">
            <h5>Возраст: от 18 до 25 лет</h5>
            <span>Посещений: 50 (33%)</span>
            <div class="clientImg">
              <img src="@/assets/images/client1.png" alt="client">
              <div class="raiting">
                <img src="@/assets/images/gold.png" alt="gold">
                <span>ТОП 1</span>
              </div>
            </div>
            <span>Любимое место</span>
            <p class="ma-0">Камера вестибюля ресторана</p>
            <span>50%</span>
            <i class="material-icons helpIcon">live_help</i>
            <v-layout class="clientMood">
              <v-flex xs3 class="iconMood">
                <span>😊</span>
              </v-flex>
              <v-flex xs9>
                <span>Настроение</span>
                <p class="ma-0">Отличное - 80%</p>
              </v-flex>
            </v-layout>
          </v-flex>
          <v-flex xs4 class="ourClientSlider-item">
            <h5>Возраст: от 18 до 25 лет</h5>
            <span>Посещений: 50 (33%)</span>
            <div class="clientImg">
              <img src="@/assets/images/client1.png" alt="client">
              <div class="raiting">
                <img src="@/assets/images/gold.png" alt="gold">
                <span>ТОП 1</span>
              </div>
            </div>
            <span>Любимое место</span>
            <p class="ma-0">Камера вестибюля ресторана</p>
            <span>50%</span>
            <i class="material-icons helpIcon">live_help</i>
            <v-layout class="clientMood">
              <v-flex xs3 class="iconMood">
                <span>😊</span>
              </v-flex>
              <v-flex xs9>
                <span>Настроение</span>
                <p class="ma-0">Отличное - 80%</p>
              </v-flex>
            </v-layout>
          </v-flex>
          <v-flex xs4 class="ourClientSlider-item">
            <h5>Возраст: от 18 до 25 лет</h5>
            <span>Посещений: 50 (33%)</span>
            <div class="clientImg">
              <img src="@/assets/images/client1.png" alt="client">
              <div class="raiting">
                <img src="@/assets/images/gold.png" alt="gold">
                <span>ТОП 1</span>
              </div>
            </div>
            <span>Любимое место</span>
            <p class="ma-0">Камера вестибюля ресторана</p>
            <span>50%</span>
            <i class="material-icons helpIcon">live_help</i>
            <v-layout class="clientMood">
              <v-flex xs3 class="iconMood">
                <span>😊</span>
              </v-flex>
              <v-flex xs9>
                <span>Настроение</span>
                <p class="ma-0">Отличное - 80%</p>
              </v-flex>
            </v-layout>
          </v-flex>
        </v-layout>
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
      <v-flex class="materialBox pl-0 pr-0" xs5>
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
            <div class="mainChartContainer">
              <v-btn class="addEventBtn" color="white" @click="addEvenShow = !addEvenShow">
                <v-icon class="mr-2" color="purple">list</v-icon>Добавить событие
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
                    <v-date-picker
                      v-model="date"
                      no-title
                      scrollable
                      color="primary"
                      header-color="red"
                    >
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
              <apexchart
                ref="chart"
                height="400"
                type="line"
                :options="lineOptions"
                :series="series"
              ></apexchart>
            </div>
          </v-flex>
          <v-flex class="mt-3 ml-2" xs3>
            <analitic-stat></analitic-stat>
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
import ChartBar from "../components/chart/ChartBar";
import HeatMap from "../components/analitics/HeatMap";
import AnaliticStat from "../components/analitics/AnaliticStat";
import AnaliticTable from "../components/analitics/AnaliticTable";
import AnaliticLineChart from "../components/analitics/AnaliticLineChart";

export default {
  name: "Analitics",
  components: {
    ChartBar,
    HeatMap,
    AnaliticLineChart,
    AnaliticStat,
    AnaliticTable
  },
  data() {
    return {
      date: new Date().toISOString().substr(0, 10),
      datePicker: false,
      addEvenShow: false,
      textAreaVal: "",
      areaError: false,
      groupBy: ["Все", "Сегодня", "Неделя", "Месяц", "3 месяца"],
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
                stepSize: 25
              },
              gridLines: {
                borderDash: ["5", "4"]
              }
            }
          ]
        },
        legend: { display: false }
      },
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
          },
          events: {
            click: function(event, chartContext, config) {
              console.log(event, chartContext, config);
              
            }
          }
        },
        tooltip: {
        },
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
        let date = new Date(this.date).toLocaleString("en-US").substr(0, 9);
        this.areaError = false;
        this.$refs.chart.addXaxisAnnotation({
          x: new Date(date).getTime(),
          strokeDashArray: 0,
          borderColor: "#775DD0",
          label: {
            borderColor: "#775DD0",
            style: {
              color: "#fff",
              background: "#775DD0"
            },
            orientation: "horizontal",
            text: this.textAreaVal
          }
        });
      }
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
.ourClientSlider {
  text-align: center;
  font-size: 9px;
  color: #969696;
  padding-top: 10px;
}
.ourClientSlider-item {
  border-right: 1px solid #d4d4d4;
  padding: 5px;
}
.ourClientSlider-item:last-child {
  border-right: none;
}
.ourClientSlider h5 {
  font-size: 11px;
  color: #000;
  font-weight: 400;
}
.clientImg {
  position: relative;
}
.raiting {
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #000;
  font-size: 12px;
}
.clientImg img {
  height: 150px;
  width: auto;
}
.raiting img {
  width: 35px;
  height: auto;
}
.iconMood {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 18px;
}
.clientMood {
  border-top: 1px solid #d4d4d4;
  padding: 5px 0;
}
.clientMood p {
  font-size: 12px;
  color: #000;
}
.helpIcon {
  font-size: 12px;
  color: #7d6df2;
  margin-left: 10px;
}
.smallGreyText {
  text-align: center;
  font-size: 10px;
  color: #969696;
  margin-bottom: 0;
}
/* checkbox styling */

.statCheckbox {
  position: relative;
}

.statCheckbox input[type="checkbox"] + label:before {
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

.statCheckbox input[type="checkbox"]:checked + label:before {
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

.statCheckbox input[type="checkbox"]:checked + label:after {
  font-weight: bold;
  content: "⅃";
  position: absolute;
  transform: rotate(45deg);
  left: 13px;
  top: 4px;
  font-size: 16px;
  color: #fff;
}

.statCheckbox input[type="checkbox"]:focus + label::before {
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
</style>

