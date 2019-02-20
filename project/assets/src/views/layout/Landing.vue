<template>
    <v-app>
        <landing-header></landing-header>

        <router-view></router-view>

        <modal-login :dialog="login"></modal-login>
        <modal-register :dialog="register"></modal-register>
        <modal-forgot-pass :dialog="forgot_password"></modal-forgot-pass>

        <landing-footer></landing-footer>
    </v-app>
</template>

<script>
    import LandingHeader from './../../components/layout/landing/Header'
    import LandingFooter from './../../components/layout/landing/Footer'

    import Login from '../../components/modals/auth/LoginModal'
    import Register from '../../components/modals/auth/RegisterModal'
    import ForgotPassword from '../../components/modals/auth/ForgotPasswordModal'

    export default {
        name: "get-face-landing",
        beforeCreate() {
            if (sessionStorage.getItem('token') || localStorage.getItem('token')) {
                let user = this.$store.getters['auth/user'];

                if (!user || !user.id) {
                    this.$http('auth.user')
                        .then(res => {
                            this.$store.commit('auth/setUser', res.data);
                            this.$router.push({name: 'dashboard'});
                        })
                        .catch(err => {
                            this.$store.dispatch('auth/logout').catch(e => {
                                /* just do nothing */
                            });
                        })
                }
            }
        },
        beforeMount() {
            this.$bus.$on('get-face-login-modal', this.callLoginModal);
            this.$bus.$on('get-face-login-modal-state', this.setLoginModalState);

            this.$bus.$on('get-face-register-modal', this.callRegisterModal);
            this.$bus.$on('get-face-register-modal-state', this.setRegisterModalState);

            this.$bus.$on('get-face-forgot-password-modal', this.callForgotPasswordModal);
            this.$bus.$on('get-face-forgot-password-modal-state', this.setForgotPasswordModalState);
        },
        data() {
            return {
                login: false,
                register: false,
                forgot_password: false,
            }
        },
        components: {
            'landing-header': LandingHeader,
            'landing-footer': LandingFooter,

            'modal-login': Login,
            'modal-register': Register,
            'modal-forgot-pass': ForgotPassword,
        },
        methods: {
            callLoginModal() {
                this.login = true;
            },
            setLoginModalState(payload) {
                this.login = payload[0];
            },
            callRegisterModal() {
                this.register = true;
            },
            setRegisterModalState(payload) {
                this.register = payload[0];
            },
            callForgotPasswordModal() {
                this.forgot_password = true;
            },
            setForgotPasswordModalState(payload) {
                this.forgot_password = payload[0];
            },
        }
    }
</script>
