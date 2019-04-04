<template>
    <v-toolbar fixed dence class="thin-toolbar" color="white">

        <v-flex xs2>
            <get-face-header-companies></get-face-header-companies>
        </v-flex>

        <v-btn class="mr-5" icon @click="userSelfUpdate">
            <v-icon color="grey lighten-1">
                refresh
            </v-icon>
        </v-btn>

        <v-spacer v-if="display_search"><!-- SPACER --></v-spacer>

        <v-flex xs3>
            <get-face-header-search v-if="display_search" class="hidden-xs-and-down"></get-face-header-search>
        </v-flex>

        <v-spacer v-if="display_search"><!-- SPACER --></v-spacer>

        <v-icon
                v-if="is_manager"
                x-large
                color="grey lighten-1"
                class="rotate90">
            battery_std
        </v-icon>

        <v-spacer v-if="display_search"><!-- SPACER --></v-spacer>

        <!-- ToDo: move this shit into toolbox -->
        <v-btn class="mr-5" icon @click="toggleAside" v-if="$vuetify.breakpoint.xs">
            <v-icon color="grey darken-2">
                code
            </v-icon>
        </v-btn>

        <get-face-header-payment v-show="is_owner"></get-face-header-payment>

        <v-spacer v-if="display_search"><!-- SPACER --></v-spacer>

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
            display_search: {
                get() {
                    return this.is_manager && !this.$vuetify.breakpoint.mdAndDown;
                },
            }
        },
    }
</script>

<style scoped>
    .thin-toolbar {
        max-width: 80vw;
        left: 10vw;
        border-bottom-right-radius: 5px;
        border-bottom-left-radius: 5px;
    }

    @media (max-width: 1048px) {
        .thin-toolbar {
            max-width: 100vw;
            left: 0;
            border-radius: 0;
        }
    }

    .rotate90 {
        transform: rotateZ(90deg);
    }
</style>
