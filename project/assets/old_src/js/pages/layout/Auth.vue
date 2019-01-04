<template>
    <div>
        <v-tabs
                fixed-tabs
                slider-color="cyan darken-1"
                active-class="active"
        >
            <v-tab :to="{name:'auth.login'}">
                Вход
            </v-tab>
            <v-tab :to="{name:'auth.register'}">
                Регистрация
            </v-tab>
        </v-tabs>
        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        name: "abn-auth",
        data() {
            return {
                active: null,
            };
        },
        methods: {},
    }
</script>