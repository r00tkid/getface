<template>
    <v-container grid-list-md text-xs-center fluid class="home-wrap">
        <v-layout row wrap justify-end>
            <v-flex xs6 d-flex>
                <v-btn outline color="grey">23 янв 2019</v-btn>
                <v-btn outline color="grey">23 фев 2019</v-btn>

                <v-btn large outline color="grey">Сегодня</v-btn>
                <v-btn large outline color="grey">Неделя</v-btn>
                <v-btn large outline color="purple"> Месяц</v-btn>
                <v-btn large outline color="grey">Год</v-btn>
            </v-flex>
        </v-layout>
        <v-layout row wrap justify-start>
            <v-flex xs6>
                <v-data-iterator
                        :items="items"
                        :rows-per-page-items="rowsPerPageItems"
                        :pagination.sync="pagination"
                        content-tag="v-layout"
                        hide-actions
                        row
                        wrap
                >

                    <v-flex
                            slot="item"
                            slot-scope="props"
                            xs12
                            sm6
                            md4
                            lg3
                    >
                        <v-card>
                            <v-card-title class="subheading font-weight-bold">{{ props.item.name }}</v-card-title>
                            <v-card-title>{{ props.item.name }}</v-card-title>

                            <v-divider></v-divider>

                            <v-list dense>
                                <v-list-tile>
                                    <v-list-tile-content>Calories:</v-list-tile-content>
                                    <v-list-tile-content class="align-end">{{ props.item.calories }}
                                    </v-list-tile-content>
                                </v-list-tile>

                                <v-list-tile>
                                    <v-list-tile-content>Fat:</v-list-tile-content>
                                    <v-list-tile-content class="align-end">{{ props.item.fat }}</v-list-tile-content>
                                </v-list-tile>
                            </v-list>
                        </v-card>
                    </v-flex>
                </v-data-iterator>
            </v-flex>
            <v-flex xs2>
                <v-card class="kill-card mt-3" dense>
                    <v-layout row justify-center>
                        <v-flex xs12>
                            <v-card-title class="justify-center">
                                <div class="headline ">Разница <br> План/Факт</div>
                            </v-card-title>
                        </v-flex>
                    </v-layout>
                    <v-divider light></v-divider>
                    <v-card-actions class="pa-3 green--text justify-center">
                        +20 ч : 30 м
                    </v-card-actions>
                </v-card>
                <v-card class="kill-card mt-3">
                    <v-layout row justify-center>
                        <v-flex xs12>
                            <v-card-title class="justify-center">
                                <div class="headline ">Разница <br> План/Факт</div>
                            </v-card-title>
                        </v-flex>
                    </v-layout>
                    <v-divider light></v-divider>
                    <v-card-actions class="pa-3 green--text justify-center">
                        +20 ч : 30 м
                    </v-card-actions>
                </v-card>
                <v-card class="kill-card mt-3">
                    <v-layout row justify-center>
                        <v-flex xs12>
                            <v-card-title class="justify-center">
                                <div class="headline ">Разница <br> План/Факт</div>
                            </v-card-title>
                        </v-flex>
                    </v-layout>
                    <v-divider light></v-divider>
                    <v-card-actions class="pa-3 green--text justify-center">
                        +20 ч : 30 м
                    </v-card-actions>
                </v-card>
            </v-flex>
            <v-flex xs4>
                <!--Graphs-->
            </v-flex>
        </v-layout>
        <v-layout row wrap justify-start align-baseline>
            <v-flex xs2>
                <v-select
                        class="kill-select mt-1"

                        :items="departaments"
                        solo
                        placeholder="Выбор подразделения"
                ></v-select>
            </v-flex>
            <v-flex xs2>
                <v-text-field
                        class="mt-1 normal-border"
                        single-line
                        flat
                        solo
                        label="Поиск"
                        append-icon="search"
                        color="purple"

                ></v-text-field>
            </v-flex>
            <v-flex xs6 justify-start>
                <v-chip label>
                    <span left class="mr-1">13</span>Сотрудников
                </v-chip>
                <v-chip label>
                    <v-icon color="purple">settings</v-icon>
                </v-chip>

                <v-btn color="purple lighten-1 white--text">Отправить ссылку на Face ID</v-btn>
                <v-btn color="purple lighten-1 white--text">Отправить График</v-btn>

            </v-flex>
        </v-layout>
    </v-container>
</template>
<style>
    .main-field {
        background-color: #fff;
        height: 80vh;
        border: #d4d4d4 solid 1px;
        border-radius: 8px;
    }

    .home-wrap {
        width: 80%;
    }

    .kill-card * {
        padding: 3px !important;
    }
</style>
<script>
    export default {
        name: "abn-home",
        head: {
            title() {
                return {
                    inner: 'Home',
                }
            },
        },
        data: () => ({
            departaments: [
                'test1',
                'test2',
                'test3'
            ],
            value: [
                200,
                675,
                410,
                390,
                310,
                460,
                250,
                240
            ],
            rowsPerPageItems: [4, 8, 12],
            pagination: {
                rowsPerPage: 4
            },
            items: [
                {
                    value: false,
                    name: 'Frozen Yogurt',
                    calories: 159,
                    fat: 6.0,
                    carbs: 24,
                    protein: 4.0,
                    sodium: 87,
                    calcium: '14%',
                    iron: '1%'
                },
                {
                    value: false,
                    name: 'Ice cream sandwich',
                    calories: 237,
                    fat: 9.0,
                    carbs: 37,
                    protein: 4.3,
                    sodium: 129,
                    calcium: '8%',
                    iron: '1%'
                },]
        }),
    }
</script>