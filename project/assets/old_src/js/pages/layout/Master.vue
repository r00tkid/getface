<template>
    <v-app dark>
        <abn-header></abn-header>

        <v-content>
            <router-view></router-view>
        </v-content>

        <abn-footer></abn-footer>
    </v-app>
</template>

<script>
    import Header from "$part/layout/Header"
    import Footer from "$part/layout/Footer"

    export default {
        name: "abn-master",
        components: {
            "abn-header": Header,
            "abn-footer": Footer,
        }
    }
</script>