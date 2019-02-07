<template>
    <v-app>
        <landing-header></landing-header>

        <router-view></router-view>

        <landing-footer></landing-footer>
    </v-app>
</template>

<script>
    import LandingHeader from './../../components/layout/landing/Header'
    import LandingFooter from './../../components/layout/landing/Footer'

    export default {
        name: "Landing",
        components: {
            'landing-header': LandingHeader,
            'landing-footer': LandingFooter,
        }
    }
</script>
