<template>
    <v-toolbar app>
        <v-btn icon :to="{name: 'landing'}">
            <v-icon>home</v-icon>
        </v-btn>

        <v-spacer></v-spacer>

        <v-btn icon @click="dialog=!dialog">
            <v-icon>lock_open</v-icon>
        </v-btn>
    </v-toolbar>
</template>

<script>
    import Login from '../../modals/LoginModal'
    import Register from '../../modals/RegisterModal'
    import ForgotPassword from '../../modals/ForgotPasswordModal'

    export default {
        name: "layout-header",
        components: {
            'modal-login': Login,
            'modal-register': Register,
            'modal-forgot-pass': ForgotPassword,
        },
        data() {
            return {
                dialog: false,
            };
        }
    }
</script>