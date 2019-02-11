<template>
    <v-navigation-drawer
            class="kill-sidebar"
            mini-variant
            v-model="drawer"
            height="400px"
            absolute
    >
        <v-toolbar flat class="transparent">
            <v-list class="pa-0">
                <v-list-tile avatar>
                    <v-list-tile-avatar>
                        <img src="https://randomuser.me/api/portraits/men/85.jpg">
                    </v-list-tile-avatar>

                    <v-list-tile-content>
                        <v-list-tile-title>John Leider</v-list-tile-title>
                    </v-list-tile-content>

                    <v-list-tile-action>
                        <v-btn
                                icon
                        >
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
                    :to="item.route"
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


        <v-list>
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
        data() {
            return {
                drawer: true,
                items: [
                    {title: 'Dashboard', icon: 'dashboard', route: 'dashboard'},
                    {title: 'Calendar', icon: 'calendar_today', route: 'calendar'},
                    {title: 'Profile', icon: 'account_circle', route: 'profile'},
                ],
                mini: true,
                right: null
            }
        },
        methods: {
            logout() {
                this.$store.dispatch('auth/logout').then(() => this.$router.push({name: 'landing'}))
            }
        }
    }
</script>

<style>
    /*
    todo Not like this pls
     */
    .kill-sidebar {
        margin-top: 64px !important;
        border-radius: 7px;
        /*border: 1px #dfdfdf solid;*/
        box-shadow: 0 2px 4px -1px rgba(0, 0, 0, .2), 0 4px 5px 0 rgba(0, 0, 0, .14), 0 1px 10px 0 rgba(0, 0, 0, .12);
        /*top: 50%;*/
        display: flex;
        flex-direction: column;
        /*transform: translateY(-50%) !important;*/

        /*transform: translateY(13vw) !important;*/
    }

    .primary--text.v-list__tile--active {
        color: #7d6df2 !important;
    }
</style>