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
    import Header from "./../../components/layout/Header"
    import Footer from "./../../components/layout/Footer"

    export default {
        name: "abn-master",
        components: {
            "abn-header": Header,
            "abn-footer": Footer,
        }
    }
</script>

<!-- Global project styles -->
<style lang="css">
    .input-no-arrows input[type='number'] {
        -moz-appearance: textfield !important;
    }

    .input-no-arrows input::-webkit-outer-spin-button,
    .input-no-arrows input::-webkit-inner-spin-button {
        -webkit-appearance: none !important;
    }
</style>
