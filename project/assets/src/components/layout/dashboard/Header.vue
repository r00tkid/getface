<template>
    <v-toolbar
            class="abn-header"
    >
        <v-flex xs2>
            <get-face-header-companies @companyRights="setRights"></get-face-header-companies>
        </v-flex>

        <v-spacer><!-- SPACER --></v-spacer>

        <v-flex xs3>
            <get-face-header-search v-if="has_rights"></get-face-header-search>
        </v-flex>

        <v-spacer><!-- SPACER --></v-spacer>

        <v-icon
                v-if="has_rights"
                x-large
                color="grey lighten-1"
                class="rotate90">
            battery_std
        </v-icon>

        <v-spacer><!-- SPACER --></v-spacer>

        <v-btn large outline color="grey" v-if="has_rights">12 Дней</v-btn>
        <v-btn large class="primary white--text" v-if="has_rights">Оплатить</v-btn>

        <v-spacer><!-- SPACER --></v-spacer>

        <get-face-header-notifications></get-face-header-notifications>

        <v-flex xs1>
            <get-face-header-locale></get-face-header-locale>
        </v-flex>

    </v-toolbar>
</template>

<script>
    export default {
        name: "abn-header",
        components: {
            "get-face-header-companies": () => import("./headerParts/Companies"),
            "get-face-header-search": () => import("./headerParts/Search"),
            "get-face-header-locale": () => import("./headerParts/Locale"),
            "get-face-header-notifications": () => import("./headerParts/Notifications"),
        },
        data() {
            return {
                has_rights: false,
                messages: 0,
            };
        },
        methods: {
            toggleAside() {
                this.$bus.$emit('toggle-main-side-bar');
            },
            setRights(payload) {
                this.$store.commit("auth/setRights", payload);
                this.has_rights = payload;
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
