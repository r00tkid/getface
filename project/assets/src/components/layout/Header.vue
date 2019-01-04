<template>
    <v-toolbar app>
        <!--<v-toolbar-side-icon @click.stop="true"></v-toolbar-side-icon>-->

        <v-btn icon :to="{name: 'home'}">
            <v-icon>home</v-icon>
        </v-btn>

        <v-toolbar-title class="mr-5 align-center">
            <span class="title font-weight-bold">{{ title }}</span>
        </v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon :to="{name: 'home'}" v-if="isUser()">
            <v-icon>person</v-icon>
        </v-btn>
        <v-btn icon :to="{name: 'auth.login'}" v-else>
            <v-icon>lock_open</v-icon>
        </v-btn>

        <v-btn icon @click.stop="toggleAside" v-if="isUser()">
            <v-icon>menu</v-icon>
        </v-btn>
    </v-toolbar>
</template>

<script>
    export default {
        name: "abn-header",
        data() {
            return {
                title: "Haze",
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