<template>
    <v-container align-baseline fluid class="profile-wrap">
        <v-layout row justify-space-between>
            <v-flex xs2>
                <v-select
                        flat
                        :items="items"
                        solo
                        placeholder="test"
                ></v-select>
            </v-flex>
            <v-spacer></v-spacer>
            <v-flex>
                <!--Todo fix background color and button "white" bgc-->
                <v-btn outline color="grey">Success</v-btn>
                <v-btn outline color="grey">Error</v-btn>
                <v-btn outline color="purple">Warning</v-btn>
                <v-btn outline color="grey">Info</v-btn>
            </v-flex>
            <v-flex>
                <v-btn large color="purple white--text">
                    <v-icon left dark>add_circle</v-icon>
                    Info
                </v-btn>
            </v-flex>
        </v-layout>
        <v-layout align-baseline justify-end>
            <v-flex xs2>
                <v-text-field
                        class="kill-height normal-border"
                        single-line
                        flat
                        solo
                        label="Поиск"
                        append-icon="search"
                ></v-text-field>
            </v-flex>
            <v-flex xs7>
                <v-chip label>
                    <span left class="mr-1">13</span>Сотрудников
                </v-chip>

                <v-chip label>
                    <v-icon>settings</v-icon>
                </v-chip>
                <v-btn color="purple lighten-1 white--text">Отправить ссылку на Face ID</v-btn>
                <v-btn color="purple lighten-1 white--text">Отправить график</v-btn>
            </v-flex>
            <v-flex xs3 class="d-flex justify-end">
                <v-btn color="purple lighten-1 white--text">Активные</v-btn>
                <v-btn outline color="grey">12 Дней</v-btn>
            </v-flex>
        </v-layout>
        <v-layout align-center justify-center row class="workers-data-list">
            <v-flex fill-height class="main-field ma-0">
                <v-data-table
                        v-model="data.selected"
                        hide-actions
                        :headers="data.headers"
                        :items="data.desserts"
                        total-items="100"
                        :pagination.sync="data.pagination"
                        select-all
                        item-key="name"
                        class="elevation-1 data-list-table"
                >
                    <template slot="headers" slot-scope="props">
                        <tr>
                            <th>
                                <v-checkbox
                                        :input-value="props.all"
                                        :indeterminate="props.indeterminate"
                                        primary
                                        hide-details
                                        @click="toggleAll"
                                ></v-checkbox>
                            </th>
                            <th
                                    v-for="header in props.headers"
                                    :key="header.text"
                                    :class="['column sortable', data.pagination.descending ? 'desc' : 'asc', header.value === data.pagination.sortBy ? 'active' : '']"
                                    @click="changeSort(header.value)"
                            >
                                <v-icon small>arrow_upward</v-icon>
                                {{ header.text }}
                            </th>
                        </tr>
                    </template>
                    <template slot="items" slot-scope="props">
                        <tr :active="props.selected" @click="props.selected = !props.selected">
                            <td>
                                <v-checkbox
                                        :input-value="props.selected"
                                        primary
                                        hide-details
                                ></v-checkbox>
                            </td>
                            <td class="text-xs-right">{{ props.item.fio }}</td>
                            <td class="text-xs-right">{{ props.item.rank }}</td>
                            <td class="text-xs-right">{{ props.item.warns }}</td>
                            <td class="text-xs-right">{{ props.item.leftHours }}</td>
                            <td class="text-xs-right">{{ props.item.achievement }}</td>
                            <td class="text-xs-right">{{ props.item.mood }}</td>
                            <td class="text-xs-right">{{ props.item.hourPlan }}</td>
                            <td class="text-xs-right">{{ props.item.hourFact }}</td>
                            <td class="text-xs-right">{{ props.item.workCount }}</td>
                        </tr>
                    </template>
                </v-data-table>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    // todo Disable pagination
    let data_json = {
        pagination: {
            sortBy: 'fio'
        },
        selected: [],
        headers: [
            {
                text: 'Ф.И.О.',
                align: 'left',
                value: 'fio'
            },
            {text: 'Должность', value: 'rank'},
            {text: 'Кол-во нарушений', value: 'warns'},
            {text: 'Недоработанные часы', value: 'leftHours'},
            {text: 'Награды', value: 'achievement'},
            {text: 'Настроение', value: 'mood'},
            {text: 'План рабочих часов', value: 'hourPlan'},
            {text: 'Факт отработанных часов', value: 'hourFact'},
            {text: 'Кол-во смен', value: 'workCount'},
        ],
        desserts: [
            {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            },
            {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            }, {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            }, {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            }, {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            }, {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            }, {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            }, {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            }, {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            }, {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            }, {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            }, {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            }, {
                value: false,
                fio: 'Frozen Yogurt',
                rank: "Ст. Официант",
                warns: 1,
                leftHours: 24,
                achievement: 'Da',
                mood: '76%',
                hourPlan: 2,
                hourFact: 130,
                workCount: 11,
            },
        ]
    };

    export default {
        name: "Profile",
        data() {
            return {
                items: [
                    "RUS",
                    "ENG"
                ],
                data: data_json,
            }
        }, methods: {
            toggleAll() {
                if (this.selected.length) this.selected = []
                else this.selected = this.desserts.slice()
            },
            changeSort(column) {
                if (this.pagination.sortBy === column) {
                    this.pagination.descending = !this.pagination.descending
                } else {
                    this.pagination.sortBy = column
                    this.pagination.descending = false
                }
            },
            consoleLog(item) {
                console.log(item)
            }
        }
    }
</script>

<style>

    ::-webkit-scrollbar {
        width: 0px;
        background: transparent; /* make scrollbar transparent */
    }
    .v-table__overflow {
        max-height: 60vh!important;
        overflow: scroll;
    }
    .profile-wrap {
        width: 80%;
    }
</style>