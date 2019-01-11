<template>
    <v-app>
    <v-container>
        <v-layout row wrap justify-center align-center fill-height>
            <v-flex xs6 offset-xs3>
               <router-view></router-view>
            </v-flex>
        </v-layout>
    </v-container>
        <forgot></forgot>

    </v-app>

</template>

<script>
    import LoginModal from '../components/modals/LoginModal'
    import RegisterModal from '../components/modals/RegisterModal'
    import Forgot from '../components/modals/ForgotPasswordModal'

    export default {
        name: "Auth",
        components: {
            LoginModal,
            RegisterModal,
            Forgot
        }
    }
</script>

<style scoped>

</style>