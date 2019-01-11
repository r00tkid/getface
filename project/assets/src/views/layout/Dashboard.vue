<template>
    <div>
        <v-app>
            <kill-sidebar></kill-sidebar>

            <abn-header></abn-header>
            <v-content>
                <router-view></router-view>
            </v-content>

            <abn-footer></abn-footer>
        </v-app>

    </div>
</template>

<script>
    import Header from "./../../components/layout/Header"
    import Footer from "./../../components/layout/Footer"
    import Sidebar from "./../../components/layout/Sidebar"


    export default {
        name: "abn-master",
        data: () => ({
            login: ''
        }),

        components: {
            "abn-header": Header,
            "abn-footer": Footer,
            'kill-sidebar': Sidebar
        },
        created() {
            this.login = !!this.$route.name == 'login'
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
