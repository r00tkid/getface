<template>
    <div>
        <v-layout wrap>
            <v-flex d-flex xs12>
                <v-btn class="primary lighten-1 white--text">Показать все</v-btn>
                <v-btn class="primary lighten-1">Добавить время</v-btn>
            </v-flex>
            <v-flex xs12 d-flex>
                <table class="timeTable tableOne">
                    <thead>
                    <tr class="statMainHeader">
                        <th colspan="2">Среднее время</th>
                    </tr>
                    <tr>
                        <th>прихода</th>
                        <th>ухода</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>11:00</td>
                        <td>01:00</td>
                    </tr>
                    <tr>
                        <td>11:00</td>
                        <td>01:00</td>
                    </tr>
                    <tr>
                        <td>11:00</td>
                        <td>01:00</td>
                    </tr>
                    <tr>
                        <td>11:00</td>
                        <td>01:00</td>
                    </tr>
                    <tr>
                        <td>11:00</td>
                        <td>01:00</td>
                    </tr>
                    </tbody>
                    <tfoot>
                    <tr>
                        <td colspan="2">
                            <button>⇦</button>
                        </td>
                    </tr>
                    </tfoot>
                </table>
                <table class="timeTable tableTwo">
                    <thead>
                    <tr class="statMainHeader">
                        <th colspan="2">Время по графику</th>
                    </tr>
                    <tr>
                        <th>приход</th>
                        <th>уход</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>11:00</td>
                        <td>01:00</td>
                    </tr>
                    <tr>
                        <td>11:00</td>
                        <td>01:00</td>
                    </tr>
                    <tr>
                        <td>11:00</td>
                        <td>01:00</td>
                    </tr>
                    <tr>
                        <td>11:00</td>
                        <td>01:00</td>
                    </tr>
                    <tr>
                        <td>11:00</td>
                        <td>01:00</td>
                    </tr>
                    </tbody>
                    <tfoot>
                    <tr>
                        <td colspan="2">
                            <button>⇨</button>
                        </td>
                    </tr>
                    </tfoot>
                </table>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
    export default {};
</script>

<style scoped>
    .timeTable {
        width: 100%;
        background-color: #fff;
        border-radius: 3px;
        border: 1px solid #d4d4d4;
        border-collapse: collapse;
        font-weight: 500;
    }

    .timeTable tfoot td {
        color: #7d6df2;
        font-size: 31px;
    }

    .timeTable tfoot td button {
        padding: 10px;
        width: 100%;
        outline: none;
    }

    .timeTable th, td {
        border: 1px solid #d4d4d4;
    }

    tbody td {
        padding: 10px;
    }

    .statMainHeader th {
        padding: 5px;
    }

    .tableTwo {
        border-left: 0px;
        color: #9b9b9b;
    }

    .tableOne tbody {
        color: #7d6df2;
    }
</style>
