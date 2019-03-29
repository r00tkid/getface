<template>
  <hooper :settings="hooperSettings">
    <slide>
      <div xs4 class="ourClientSlider-item">
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
        <i class="material-icons helpIcon" title="Подсказка">live_help</i>
        <v-layout class="clientMood">
          <v-flex xs3 class="iconMood">
            <span>😊</span>
          </v-flex>
          <v-flex xs9>
            <span>Настроение</span>
            <p class="ma-0">Отличное - 80%</p>
          </v-flex>
        </v-layout>
      </div>
    </slide>
    <slide>
      <div xs4 class="ourClientSlider-item">
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
        <i class="material-icons helpIcon" title="Подсказка">live_help</i>
        <v-layout class="clientMood">
          <v-flex xs3 class="iconMood">
            <span>😊</span>
          </v-flex>
          <v-flex xs9>
            <span>Настроение</span>
            <p class="ma-0">Отличное - 80%</p>
          </v-flex>
        </v-layout>
      </div>
    </slide>
    <slide>
      <div xs4 class="ourClientSlider-item">
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
        <i class="material-icons helpIcon" title="Подсказка">live_help</i>
        <v-layout class="clientMood">
          <v-flex xs3 class="iconMood">
            <span>😊</span>
          </v-flex>
          <v-flex xs9>
            <span>Настроение</span>
            <p class="ma-0">Отличное - 80%</p>
          </v-flex>
        </v-layout>
      </div>
    </slide>
    <slide>
      <div xs4 class="ourClientSlider-item">
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
        <i class="material-icons helpIcon" title="Подсказка">live_help</i>
        <v-layout class="clientMood">
          <v-flex xs3 class="iconMood">
            <span>😊</span>
          </v-flex>
          <v-flex xs9>
            <span>Настроение</span>
            <p class="ma-0">Отличное - 80%</p>
          </v-flex>
        </v-layout>
      </div>
    </slide>
    <slide>
      <div xs4 class="ourClientSlider-item">
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
        <i class="material-icons helpIcon" title="Подсказка">live_help</i>
        <v-layout class="clientMood">
          <v-flex xs3 class="iconMood">
            <span>😊</span>
          </v-flex>
          <v-flex xs9>
            <span>Настроение</span>
            <p class="ma-0">Отличное - 80%</p>
          </v-flex>
        </v-layout>
      </div>
    </slide>

    <hooper-navigation slot="hooper-addons"></hooper-navigation>
  </hooper>
</template>
<script>
import { Hooper, Slide, Navigation as HooperNavigation } from "hooper";
import "hooper/dist/hooper.css";
export default {
  components: {
    Hooper,
    Slide,
    HooperNavigation
  },
  data() {
    return {
      hooperSettings: {
        itemsToShow: 3
      }
    };
  },
  methods: {}
};
</script>
<style scoped>
.hooper {
  height: fit-content;
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
.ourClientSlider-item h5 {
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
</style>


