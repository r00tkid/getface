<template>
    <div class="TableContainer">
        <table class="timeTable">
            <tr>
                <th colspan="2" style="color: #000;">Время по графику</th>
                <th colspan="2">Среднее время</th>
            </tr>
            <tr>
                <td>приход</td>
                <td>уход</td>
                <td>прихода</td>
                <td>ухода</td>
            </tr>
            <tr>
                <td class="purpleText">11:00</td>
                <td class="purpleText">1:00</td>
                <td>11:00</td>
                <td>1:00</td>
            </tr>
            <tr>
                <td class="purpleText">11:00</td>
                <td class="purpleText">1:00</td>
                <td>11:00</td>
                <td>1:00</td>
            </tr>
        </table>
        <table class="timeTable">
            <tr>
                <th colspan="2" style="color: #000;">Время по графику</th>
                <th colspan="2">Среднее время</th>
            </tr>
            <tr>
                <td>приход</td>
                <td>уход</td>
                <td>прихода</td>
                <td>ухода</td>
            </tr>
            <tr>
                <td class="purpleText">11:00</td>
                <td class="purpleText">1:00</td>
                <td>11:00</td>
                <td>1:00</td>
            </tr>
            <tr>
                <td class="purpleText">11:00</td>
                <td class="purpleText">1:00</td>
                <td>11:00</td>
                <td>1:00</td>
            </tr>
        </table>
        <div class="timeTableControl">
            <div class="timeTableControl-arrows">
                <v-btn icon outline color="purple">&#60;</v-btn>
                <v-btn icon outline color="purple">&#62;</v-btn>
            </div>
            <div class="timeTableControl-buttons">
                <v-btn class="primary white--text">Показать все</v-btn>
                <v-btn outline color="grey">Добавить время</v-btn>
            </div>
        </div>
    </div>
</template>
<script>
    export default {};
</script>
<style scoped>
    .TableContainer {
        display: flex;
    }

    th,
    td {
        border: 1px solid #d4d4d4;
        border-collapse: collapse;
        background-color: #fff;
        padding: 2px 5px;
    }

    table {
        border-collapse: collapse;
        width: 100%;
        color: #a3a3a3;
        box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
        0 1px 5px 0 rgba(0, 0, 0, 0.12);
    }

    .timeTableControl {
        display: flex;
        background-color: #fff;
        border: #d4d4d4 solid 1px;
        box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
        0 1px 5px 0 rgba(0, 0, 0, 0.12);
        border-radius: 0 5px 5px 0;
    }

    .timeTableControl-arrows {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
        border-right: 1px solid #d4d4d4;
    }

    .timeTableControl-buttons {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
    }

    .timeTableControl-buttons button {
        text-transform: none;
        width: 140px;
    }
</style>


