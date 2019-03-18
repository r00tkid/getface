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
      <v-flex class="materialBox" xs5>
        <h4>Количество клиентов по времени</h4>
        <p class="mb-1">
          Среднее количество:
          <span>450 чел.</span>
        </p>
        <span class="devider"></span>
        <p class="smallGreyText">Количество пользователей по времени суток</p>
        <heat-map></heat-map>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ChartBar from "../components/chart/ChartBar";
import HeatMap from "../components/analitics/HeatMap";
export default {
  name: "Analitics",
  components: {
    ChartBar,
    HeatMap
  },
  data() {
    return {
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
      }
    };
  }
};
</script>

<style>
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
.groupBtn .v-input__control {
  min-height: 40px !important;
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
.smallGreyText{
  text-align: center;
  font-size: 10px;
  color: #969696;
  margin-bottom: 0;
}
</style>

