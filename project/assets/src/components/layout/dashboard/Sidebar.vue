<template>
    <v-navigation-drawer
            class="kill-sidebar"
            v-model="drawer"
            :height="400"
            :mobile-break-point="720"
            mini-variant
            fixed
            app
    >
        <v-toolbar flat class="transparent">
            <v-list class="pa-0">
                <v-list-tile avatar>
                    <v-list-tile-avatar>
                        <img :src="face">
                    </v-list-tile-avatar>

                    <v-list-tile-content>
                        <v-list-tile-title>John Leider</v-list-tile-title>
                    </v-list-tile-content>

                    <v-list-tile-action>
                        <v-btn icon>
                            <v-icon>chevron_left</v-icon>
                        </v-btn>
                    </v-list-tile-action>
                </v-list-tile>
            </v-list>
        </v-toolbar>

        <v-list class="pt-0">
            <v-divider></v-divider>

            <v-list-tile
                    v-for="item in items"
                    :key="item.title"
                    :to="{name: item.name}"
            >
                <v-list-tile-action>
                    <v-icon>{{ item.icon }}</v-icon>
                </v-list-tile-action>

                <v-list-tile-content>
                    <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                </v-list-tile-content>
            </v-list-tile>
        </v-list>

        <v-spacer></v-spacer>

        <v-list style="justify-self: end">
            <v-list-tile @click="logout">
                <v-list-tile-action>
                    <v-icon>logout</v-icon>
                </v-list-tile-action>

                <v-list-tile-content>
                    <v-list-tile-title>Logout</v-list-tile-title>
                </v-list-tile-content>
            </v-list-tile>
        </v-list>

    </v-navigation-drawer>
</template>

<script>
    export default {
        name: "Sidebar",
        mounted() {
            this.$bus.$on('toggle-main-side-bar', this.toggleMe);
        },
        data() {
            return {
                drawer: true,
                items: [
                    {title: 'Dashboard', icon: 'dashboard', name: 'dashboard.main'},
                    {title: 'Calendar', icon: 'calendar_today', name: 'dashboard.calendar'},
                    {title: 'Profile', icon: 'account_circle', name: 'dashboard.profile'},
                    {title: 'Cameras', icon: 'camera', name: 'dashboard.cameras'},
                ],
                mini: true,
                right: null,
            }
        },
        methods: {
            logout() {
                this.$store.dispatch('auth/logout').then(() => this.$router.push({name: 'landing'}))
            },
            toggleMe() {
                this.drawer = !this.drawer;
            },
        },
        computed: {
            face: {
                get() {
                    return `https://randomuser.me/api/portraits/thumb/${Math.random() > 0.51 ? "men" : "women"}/${(Math.random() * 100) | 0}.jpg`;
                },
            },
        }
    }
</script>

<style scoped>
    .kill-sidebar {
        display: flex;
        flex-flow: column nowrap;
        box-shadow: 0 2px 4px -1px rgba(0, 0, 0, .2), 0 4px 5px 0 rgba(0, 0, 0, .14), 0 1px 10px 0 rgba(0, 0, 0, .12);
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        transform: translate(0, 50%) !important;
    }

    .kill-sidebar.v-navigation-drawer--is-mobile.v-navigation-drawer--open {
        transform: translate(0, 50%) !important;
    }

    .kill-sidebar.v-navigation-drawer--is-mobile {
        transform: translate(-101%, 50%) !important;
    }
</style>

<style>
    .kill-sidebar .primary--text.v-list__tile--active {
        color: #7d6df2 !important;
    }
</style>
