<template>
    <v-toolbar app>

        <v-btn icon :to="{name: 'landing'}">
            <v-icon>home</v-icon>
        </v-btn>

        <v-spacer></v-spacer>

        <v-btn icon @click="changeLoginState">
            <v-icon>lock_open</v-icon>
        </v-btn>

    </v-toolbar>
</template>

<script>
    export default {
        name: "layout-header",
        data() {
            return {};
        },
        methods: {
            changeLoginState() {
                this.$bus.$emit('get-face-login-modal');
            },
        }
    }
</script>