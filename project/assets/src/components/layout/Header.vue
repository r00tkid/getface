<template>
    <v-toolbar
            class="abn-header"
    >
        <v-flex xs2>
            <v-select
                    class="kill-select mt-1"
                    flat
                    :items="companies"
                    solo
                    v-model="defaultCompany"
            ></v-select>
        </v-flex>

        <v-spacer></v-spacer>
        <v-flex xs3>
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
        <v-spacer></v-spacer>
        <v-icon
                x-large
                color="grey lighten-1"
                class="rotate90"
        >
            battery_std
        </v-icon>
        <v-spacer></v-spacer>
        <v-btn large outline color="grey">12 Дней</v-btn>
        <v-btn large color="purple lighten-1 white--text">Оплатить</v-btn>
        <v-spacer></v-spacer>

        <v-badge left class="mr-5">
            <!--<span slot="badge">6</span>-->
            <v-icon
                    large
                    color="grey lighten-1"
            >
                notification_important
            </v-icon>
        </v-badge>

        <v-flex xs1>
            <v-select
                    class="kill-select"
                    flat
                    :items="items"
                    solo
                    v-model="defaultLang"
            ></v-select>
        </v-flex>

    </v-toolbar>
</template>

<script>
    export default {
        name: "abn-header",
        data() {
            return {
                defaultCompany: 'Company 1',
                defaultLang: 'ENG',
                title: "Haze",
                items: [
                    "RUS",
                    "ENG"
                ],
                companies: [
                    'Company 1',
                    'Company 2',
                    'Company 3',
                ]
            };
        },
        methods: {
            toggleAside() {
                this.$bus.$emit('toggle-main-side-bar');
            },
            isUser() {
                return false;
            },
        },
        computed: {},
    }
</script>

<style>

    /**
    todo HELLO THIS IS GLOBAL CSS IN HEADER
     */

    .kill-select > .v-input__control > .v-input__slot {
        background-color: rgba(0, 0, 0, 0) !important;
    }

    .kill-height > .v-input__control > .v-input__slot {
        min-height: 36px!important; /* 36px because normal button has the same height. Logic. Believe me */
    }

    .normal-border > .v-input__control > .v-input__slot {
        border: 1px grey solid;
    }

    .normal-border > .v-input__control > .v-input__slot:focus {
        border: 1px purple solid!important;
    }
    .rotate90 {
        transform: rotateZ(90deg);
    }

    .abn-header {
        align-self: center;
        width: 80%;
        border-radius: 5px;
        background-color: #fff!important;
    }
</style>