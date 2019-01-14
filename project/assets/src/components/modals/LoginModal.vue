<template>
    <v-layout row justify-center>
        <v-dialog v-model="dialog" persistent max-width="500px">
            <v-card>
                <v-card-text>
                    <v-container grid-list-md>
                        <v-layout wrap align-center>
                            <v-flex xs12 class="text-xs-center dialog-header">
                                <span class="subheading bff">АВТОРИЗАЦИЯ</span>
                                <v-card-title class="justify-center">
                                    <span class="subheading">ВОЙТИ С ПОМОЩЬЮ</span>
                                </v-card-title>
                            </v-flex>
                            <v-flex xs12 class="justify-center mb-3">
                                <div class="text-xs-center">
                                    <v-btn fab dark medium color="red darken-2">
                                        <v-icon>fab fa-google-plus-g</v-icon>
                                    </v-btn>
                                    <v-btn fab dark medium color="blue">
                                        <v-icon>fab fa-vk</v-icon>
                                    </v-btn>
                                    <v-btn fab dark medium color="blue darken-3">
                                        <v-icon>fab fa-facebook-f</v-icon>
                                    </v-btn>
                                    <v-btn fab dark medium color="red">
                                        <v-icon>fab fa-yandex</v-icon>
                                    </v-btn>
                                    <v-btn fab dark medium color="blue">
                                        <v-icon color="orange" large>fas fa-at</v-icon>
                                    </v-btn>
                                </div>
                            </v-flex>
                            <v-flex xs12>
                                <v-text-field v-model="username" color="purple" prepend-icon="fas fa-user"
                                              solo
                                              label="Ваш Email/Username"
                                              required
                                ></v-text-field>
                            </v-flex>
                            <v-flex xs12>
                                <v-text-field v-model="password" color="purple" prepend-icon="vpn_key" label="Пароль"
                                              solo
                                              type="password"
                                              required
                                ></v-text-field>
                            </v-flex>
                            <v-flex xs12 d-flex>
                                <v-btn @click.prevent="submitCredentials" color="purple lighten-2" class="white--text">
                                    Войти
                                </v-btn>
                            </v-flex>
                            <v-flex xs6>
                                <v-checkbox label="Запомнить меня" v-model="checkbox1"></v-checkbox>
                            </v-flex>
                            <v-flex xs6 class="text-xs-right">
                                <a @click="openForgotPassModal">Забыли пароль?</a>
                            </v-flex>
                            <v-flex xs12 class="text-xs-center">
                                <router-link to="register">Ещё нет аккаунта?</router-link>
                            </v-flex>
                            <v-flex xs12 class="text-xs-center">
                                <p>Создавая аккаут, вы соглашаетесь с нашими <a>Правилами и условиями</a> и <a>Положением
                                    о конфиденциальности</a></p>
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-card-text>
            </v-card>
        </v-dialog>
    </v-layout>

</template>

<script>
    export default {
        name: "LoginModal",
        data() {
            return {
                checkbox1: false,
                username: '',
                password: '',
            }
        },
        computed: {
            dialog: {
                get() {
                    return this.$store.getters['modal/login'];
                },
                set(value) {
                    return this.$store.commit('modal/setLoginModal', value);
                }
            }
        },
        methods: {
            openForgotPassModal() {
                this.$store.commit('modal/setForgotPasswordModal', true);
            },
            submitCredentials() {
                let [username, password] = [this.username, this.password];
                // Do shit
                let user = this.$store.dispatch('auth/login', {username, password}).then(() => {
                    this.$router.push('dashboard')
                }).catch(() => {})
                console.log(username, password)
            }
        },
        mounted() {
            setTimeout(() => this.$store.commit('modal/setLoginModal', true), 600)
        },
        destroyed() {
            this.$store.commit('modal/setLoginModal', false);
        },

    }
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css?family=Montserrat');

    .dialog-header, .dialog-header * {
        font-family: 'Montserrat', sans-serif;
    }

    .v-card__title {
        padding-bottom: 0px;
    }

    .bff {
        font-weight: 900;
    }
</style>