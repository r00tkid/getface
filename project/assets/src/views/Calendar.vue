<template>
    <v-container class="calendar-wrap">
        <v-layout row wrap justify-end>
            <v-flex xs12 lg2 align-center class="text-xs-center">
                <div class="year-selection">
                    <v-btn icon @click="year--" small color="primary white--text">&#60;</v-btn>
                    <span class="font-weight-black title">{{year}}</span>
                    <v-btn icon @click="year++" small color="primary white--text">&#62;</v-btn>
                </div>
            </v-flex>
        </v-layout>
        <v-layout row wrap justify-end>
            <v-flex xs12>
                <v-container grid-list-xl fill-height>
                    <v-layout row wrap>
                        <v-flex xs12 md6 lg3 v-for="i in 12" >
                            <div @click="loadMonthStats(i-1)" class="vue-date-wrapper">
                                <date-pick
                                        :value="getCurrMonth(i-1)"
                                        :hasInputElement="false"
                                        :pickTime="false"
                                        :pickMinutes="false"
                                        :pickSeconds="false"
                                        :isDateDisabled="isFutureDate"
                                        :weekdays="['Пн','Вт','Ср','Чт','Пт','Сб','Вс']"
                                        :months="['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']"
                                ></date-pick>
                            </div>
                        </v-flex>
                    </v-layout>
                </v-container>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
  import DatePick from 'vue-date-pick';
  import 'vue-date-pick/dist/vueDatePick.css';

  export default {
    name: "Calendar",
    components: {
      DatePick
    },
    data() {
      return {
        date: new Date().toISOString().substr(0, 10),
        year: new Date().getFullYear().valueOf()
      }
    },
    methods: {
      getCurrMonth(month) {
        let date = new Date();
        date.setFullYear(this.year, month);
        return date.toISOString().substr(0, 10);
      },
      isFutureDate(date) {
        const currentDate = new Date();
        return date > currentDate;
      },
      loadMonthStats(e) {
        let [month, year] = [e, this.year];
        //todo implement this later
        console.log(month, year);
      }
    }
  }
</script>

<style>
    .calendar-wrap {
        width: 80%;
    }

    .vdpArrow {
        display: none;
    }

    .vdpPeriodControls > div:nth-child(2), .vdpPeriodControl > select {
        display: none;
    }

    .vue-date-wrapper, .vdpInnerWrap, .vdpComponent, .vdpOuterWrap {
        height: 100%;
    }
    .vue-date-wrapper {
        cursor: pointer;
    }

    .vdpHeader {
        background-image: linear-gradient(to right top, #7d6df2, #9077f4, #a181f6, #b08bf9, #be96fb);;
        color: white;
        font-weight: 700;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }

    .vdpTable .vdpHeadCellContent {
        color: unset;
    }

    .vdpCell.selected .vdpCellContent {
        background-color: unset;
        color: unset;
    }


    .year-selection {
        margin-right: 24px;
        padding: 5px;
        background-color: rgba(256, 256, 256, 0.8);
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: baseline;
        border: 1px solid #b2b2b2;
        border-radius: 4px;
    }

    @media screen and (max-width: 1264px) {
        .year-selection {
            margin: 0 24px;
        }
    }
</style>