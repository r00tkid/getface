<template>
    <v-container align-baseline fluid class="profile-wrap">
        <v-layout row justify-end>
            <v-flex>
                <v-select flat :items="items" solo placeholder="test" class="width-fixer"></v-select>
            </v-flex>
            <v-spacer></v-spacer>
            <v-flex class="d-flex justify-end">
                <!--Todo fix background color and button "white" bgc-->
                <v-btn outline color="grey">Сегодня</v-btn>
                <v-btn outline color="grey">Неделя</v-btn>
                <v-btn outline color="purple">Месяц</v-btn>
                <v-btn outline color="grey">Год</v-btn>
            </v-flex>
            <v-spacer></v-spacer>
            <v-flex class="d-flex width-limiter">
                <v-btn large color="primary white--text">
                    <v-icon left dark>add_circle</v-icon>
                    Добавить сотрудника
                </v-btn>
            </v-flex>
        </v-layout>
        <v-layout align-baseline justify-end>
            <v-flex>
                <v-text-field
                        class="kill-height normal-border width-fixer"
                        single-line
                        flat
                        solo
                        label="Поиск"
                        append-icon="search"
                        color="purple"
                ></v-text-field>
            </v-flex>
            <v-flex d-flex>
                <v-chip label>
                    <span left class="mr-1">13</span>Сотрудников
                </v-chip>

                <v-chip label>
                    <v-icon color="purple">settings</v-icon>
                </v-chip>

                <v-btn outline color="grey">Создать зону видимости</v-btn>
                <v-btn class="primary white--text">Отправить логин и пароль</v-btn>
            </v-flex>
            <v-flex>
                <v-btn outline color="grey">Выгрузить в Excel</v-btn>
            </v-flex>
            <v-flex class="d-flex justify-end width-limiter">
                <v-btn class="primary white--text">Активные</v-btn>
                <v-btn color="error lighten-1">Уволенные</v-btn>
            </v-flex>
        </v-layout>
        <v-layout align-center justify-center row class="workers-data-list">
            <v-flex fill-height class="ma-0">
                <profile-table></profile-table>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import ProfileTable from "../components/profileTable/ProfileTable";

    export default {
        name: "Profile",
        components: {
            ProfileTable
        },
        data() {
            return {
                items: ["RUS", "ENG"],
                data: {}
            };
        },
        methods: {
            toggleAll() {
                if (this.selected.length) this.selected = [];
                else this.selected = this.desserts.slice();
            },
            changeSort(column) {
                if (this.pagination.sortBy === column) {
                    this.pagination.descending = !this.pagination.descending;
                } else {
                    this.pagination.sortBy = column;
                    this.pagination.descending = false;
                }
            },
            hideGroup(e) {
                if (e.target.className.includes("tableSeparator")) {
                    let tableBody = e.target.parentElement.parentElement;
                    let bodyElements = tableBody.childNodes;

                    bodyElements.forEach((element, i) => {
                        if (i > 0 && element.style.display == "none") {
                            element.style.display = "table-row";
                        } else if (i > 0) {
                            element.style.display = "none";
                        }
                    });
                }
            }
        }
    };
</script>

<style scoped>
    .container {
        padding: 24px 0;
    }

    .tableContainer {
        overflow: auto;
        max-height: 500px;
    }

    .v-table__overflow {
        max-height: 70vh !important;
        overflow: scroll;
    }

    .profile-wrap {
        width: 80%;
    }

    table.v-table thead th:not(:first-child) {
        white-space: pre-line;
    }

    .width-fixer {
        max-width: 190px;
    }

    .width-limiter {
        max-width: 290px;
    }

    th,
    td {
        border: 1px solid #d4d4d4;
        border-collapse: collapse;
        background-color: #fff;
        padding: 10px;
    }

    table {
        border-collapse: collapse;
        min-width: 1270px;
        box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
        0 1px 5px 0 rgba(0, 0, 0, 0.12);
    }

    .tableSeparator {
        background-color: #a841ba;
        color: #fff;
        padding: 5px 40px;
        cursor: pointer;

    }

    .separatorText {
        position: relative;
    }

    .separatorText::after {
        content: "";
        position: absolute;
        top: 7px;
        right: -10px;
        width: 0;
        height: 0;
        border-style: solid;
        border-width: 5px 2.5px 0 2.5px;
        border-color: #ffffff transparent transparent transparent;
    }

    .reward {
        font-size: 25px;
        color: #f6a944;
    }

    .mood {
        font-size: 25px;
        color: #5ae08f;
    }

    .tableContainer::-webkit-scrollbar {
        width: 5px;
        height: 5px;
    }

    .tableContainer::-webkit-scrollbar-button {
        display: none;
    }

    .tableContainer::-webkit-scrollbar-track {
        background-color: #969696;
    }

    .tableContainer::-webkit-scrollbar-track-piece {
        background-color: #d4d4d4;
    }

    .tableContainer::-webkit-scrollbar-thumb {
        height: 50px;
        background-color: #969696;
        border-radius: 3px;
    }

    .tableContainer::-webkit-scrollbar-corner {
        display: none;
    }

    .tableContainer::-webkit-resizer {
        background-color: #969696;
    }
</style>