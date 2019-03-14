<template>
    <v-toolbar
            class="abn-header"
    >
        <v-flex xs2>
            <get-face-header-companies></get-face-header-companies>
        </v-flex>

        <v-btn class="mr-5" icon @click="userSelfUpdate">
            <v-icon color="grey lighten-1">
                refresh
            </v-icon>
        </v-btn>

        <v-spacer><!-- SPACER --></v-spacer>

        <v-flex xs3>
            <get-face-header-search v-if="is_manager"></get-face-header-search>
        </v-flex>

        <v-spacer><!-- SPACER --></v-spacer>

        <v-icon
                v-if="is_manager"
                x-large
                color="grey lighten-1"
                class="rotate90">
            battery_std
        </v-icon>

        <v-spacer><!-- SPACER --></v-spacer>

        <get-face-header-payment v-if="is_owner"></get-face-header-payment>

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
            "get-face-header-notifications": () => import("./headerParts/Notifications"),
            "get-face-header-companies": () => import("./headerParts/Companies"),
            "get-face-header-payment": () => import("./headerParts/Payment"),
            "get-face-header-search": () => import("./headerParts/Search"),
            "get-face-header-locale": () => import("./headerParts/Locale"),
        },
        beforeMount() {
            this.$bus.$on("get-face-company-changed", this.setRights);
        },
        data() {
            return {
                owner: false,
                manager: false,
                messages: 0,
            };
        },
        methods: {
            toggleAside() {
                this.$bus.$emit('toggle-main-side-bar');
            },
            setRights(company) {
                if (!company) {
                    this.is_owner = false;
                    this.is_manager = false;

                    return;
                }

                this.is_owner = company.rights ? company.rights.is_owner : false;
                this.is_manager = company.rights ? company.rights.is_manager : false;
            },
            userSelfUpdate() {
                this.$bus.$emit("get-face-user-self-update");
            },
        },
        computed: {
            is_owner: {
                get() {
                    return this.owner;
                },
                set(bool) {
                    this.owner = bool;
                },
            },
            is_manager: {
                get() {
                    return this.manager;
                },
                set(bool) {
                    this.manager = bool;
                },
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
