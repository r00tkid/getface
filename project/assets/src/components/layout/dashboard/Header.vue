<template>
    <v-toolbar
            class="abn-header"
    >
        <v-flex xs2>
            <get-face-companies></get-face-companies>
        </v-flex>

        <v-spacer><!-- SPACER --></v-spacer>

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

        <v-spacer><!-- SPACER --></v-spacer>

        <v-icon
                x-large
                color="grey lighten-1"
                class="rotate90"
        >
            battery_std
        </v-icon>

        <v-spacer><!-- SPACER --></v-spacer>

        <v-btn large outline color="grey">12 Дней</v-btn>
        <v-btn large class="primary white--text">Оплатить</v-btn>

        <v-spacer><!-- SPACER --></v-spacer>

        <v-btn left class="mr-5" icon>
            <span slot="badge">6</span>
            <v-icon
                    large
                    color="grey lighten-1"
            >
                notification_important
            </v-icon>
        </v-btn>

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
        components: {
            "get-face-companies": () => import("./headerParts/Companies")
        },
        data() {
            return {
                defaultLang: 'ENG',
                title: "Haze",
                items: [
                    "RUS",
                    "ENG"
                ],
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
    }
</script>

<style scoped>
    /* todo: do */
    .kill-select > .v-input__control > .v-input__slot {
        background-color: rgba(0, 0, 0, 0) !important;
    }

    .kill-height > .v-input__control > .v-input__slot {
        min-height: 36px !important; /* 36px because normal button has the same height. Logic. Believe me */
    }

    .normal-border > .v-input__control > .v-input__slot {
        border: 1px grey solid;
    }

    .normal-border > .v-input__control > .v-input__slot:focus {
        border: 1px purple solid !important;
    }

    .rotate90 {
        transform: rotateZ(90deg);
    }

    .abn-header {
        align-self: center;
        width: 80%;
        border-radius: 5px;
        background-color: #fff !important;
    }
</style>