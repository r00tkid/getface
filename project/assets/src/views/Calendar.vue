<template>
    <v-container grid-list-xl fill-height class="calendar-wrap">
        <v-layout row wrap>
            <v-flex xs3 v-for="i in 12">
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
                date: new Date().toISOString().substr(0, 10)
            }
        },
        methods: {
            getCurrMonth(month) {
                let date = new Date();
                date.setFullYear(new Date().getFullYear(), month);
                return date.toISOString().substr(0, 10);
            },
            isFutureDate(date) {
                const currentDate = new Date();
                return date > currentDate;
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

    .vdpInnerWrap, .vdpComponent, .vdpOuterWrap {
        height: 100%;
    }

    .vdpHeader {
        background-color: #ab47bc;
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

    /*.vdpTable > thead {*/
    /*display: none;*/
    /*}*/
</style>