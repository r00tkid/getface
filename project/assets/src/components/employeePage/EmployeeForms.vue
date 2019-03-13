<template>
    <v-layout row wrap>
        <v-flex class="empoloyeeForms" lg12>
            <v-text-field
                    class="input-shadow"
                    background-color="white"
                    color="purple"
                    solo
                    label="Имя"
                    outline
                    hide-details
            ></v-text-field>
            <v-text-field
                    class="input-shadow"
                    background-color="white"
                    color="purple"
                    solo
                    label="Фамилия"
                    hide-details
            ></v-text-field>
            <v-text-field
                    class="input-shadow"
                    background-color="white"
                    color="purple"
                    solo
                    label="Отчество"
                    hide-details
            ></v-text-field>
            <v-select :items="duties" label="Должность" solo v-model="duty" hide-details>
                <template slot="append">
                    <v-icon color="purple">fas fa-chevron-circle-right</v-icon>
                </template>
            </v-select>
            <v-select :items="duties" label="Подразделение" solo v-model="duty" hide-details>
                <template slot="append">
                    <v-icon class="purple--text">fas fa-chevron-down</v-icon>
                </template>
            </v-select>
            <v-text-field
                    class="input-shadow"
                    background-color="white"
                    color="purple"
                    type="tel"
                    prefix="+"
                    mask="# (###) ###-##-##"
                    placeholder="7 (999) 999-99-99"
                    solo
                    label="Телефон"
                    hide-details
            ></v-text-field>
            <v-text-field
                    class="input-shadow"
                    background-color="white"
                    color="purple"
                    type="email"
                    placeholder="infor@example.com"
                    solo
                    label="Email"
                    hide-details
            ></v-text-field>

            <v-layout>
                <v-flex xs5>
                    <v-menu
                            ref="datePicker"
                            :close-on-content-click="false"
                            v-model="datePicker"
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
                        <v-date-picker v-model="date" no-title scrollable color="primary" header-color="red">
                            <v-spacer></v-spacer>
                            <v-btn flat color="purple" @click="datePicker = false">Cancel</v-btn>
                            <v-btn flat color="purple" @click="$refs.datePicker.save(date)">OK</v-btn>
                        </v-date-picker>
                    </v-menu>
                </v-flex>
                <v-flex xs7 class="gender">
                    <v-radio-group v-model="gender" row>
                        <v-radio label="Мужчина" value="man"></v-radio>
                        <v-radio label="Женщина" value="woman"></v-radio>
                    </v-radio-group>
                </v-flex>
            </v-layout>
        </v-flex>
    </v-layout>
</template>

<script>
    export default {
        data() {
            return {
                gender: "man",
                date: new Date().toISOString().substr(0, 10),
                datePicker: false,
                duties: ["Первая должность", "Вторая", "Третья"],
                duty: "Первая должность",
            }
        }
    };
</script>

<style scoped>
    .empoloyeeForms .v-input {
        margin-bottom: 15px;
    }

    .v-input--selection-controls .v-input__slot {
        border: none !important;
    }

    .v-input--selection-controls .v-label {
        font-size: 13px;
    }

    .v-input--selection-controls .v-radio {
        margin-right: 10px;
    }

    .v-input--selection-controls .accent--text {
        color: #7d6df2 !important;
    }

    .v-menu__activator .v-input__control {
        margin-bottom: 0;
    }

    .v-input--selection-controls .v-input__control {
        margin-bottom: 0;
    }

    .v-menu__activator .v-input__slot {
        height: 47px;
    }

    .v-input__slot {
        min-height: 30px !important;
        border-radius: 4px !important;
    }

    .v-input input {
        max-height: 25px !important;
    }

    .v-text-field--box .v-label {
        top: 15px;
        font-weight: 500;
        font-size: 14px;
    }

    .v-select__selections {
        line-height: 32px;
    }
</style>
