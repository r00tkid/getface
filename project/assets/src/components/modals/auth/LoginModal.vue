<template>
    <v-layout row justify-center :if="dialog">
        <v-dialog v-model="modalState" max-width="500px" @keydown.esc="modalState = false">
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
                                <v-text-field v-model="username" color="purple" prepend-inner-icon="fas fa-user"
                                              label="Ваш Email/Username"
                                              @keydown.space.prevent
                                              @keyup.enter="$refs.passwordField.focus()"
                                              class="input-shadow"
                                              background-color="white"
                                              box
                                              required
                                ></v-text-field>
                            </v-flex>
                            <v-flex xs12>
                                <v-text-field v-model="password" color="purple"
                                              ref="passwordField"
                                              @keyup.enter="submitCredentials"
                                              prepend-inner-icon="vpn_key"
                                              label="Пароль"
                                              class="input-shadow"
                                              background-color="white"
                                              box
                                              type="password"
                                              required
                                ></v-text-field>
                            </v-flex>
                            <v-flex xs12 d-flex>
                                <v-btn :loading="checkin"
                                       :disabled="checkin"
                                       @click="submitCredentials"
                                       @click.prevent="preventLogin"
                                       color="primary lighten-2"
                                       class="white--text">
                                    Войти
                                </v-btn>
                            </v-flex>
                            <v-flex xs12 sm6 class="text-xs-center text-sm-right">
                                <a @click="openForgotPassModal">Забыли пароль?</a>
                            </v-flex>
                            <v-flex xs12 sm6 class="text-xs-center text-sm-left">
                                <a @click="openRegisterModal">Ещё нет аккаунта?</a>
                            </v-flex>
                            <v-flex xs12 class="text-xs-center">
                                <p>
                                    Создавая аккаут, вы соглашаетесь с нашими
                                    <a>Правилами и условиями</a> и
                                    <a>Положением о конфиденциальности</a>
                                </p>
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
        name: "get-face-login",
        props: {
            dialog: {
                type: Boolean,
                default: false,
            }
        },
        data() {
            return {
                checkin: false,
                username: '',
                password: '',
            }
        },
        methods: {
            openForgotPassModal() {
                this.modalState = false;
                this.$bus.$emit('get-face-forgot-password-modal');
            },
            openRegisterModal() {
                this.modalState = false;
                this.$bus.$emit('get-face-register-modal');
            },
            submitCredentials() {
                this.checkin = true;

                this.$http('auth.login', window.collections.collectObject(this.$data, 'username', 'password'), 'post')
                    .then((res) => {
                        this.$store.commit('auth/setToken', {token: res.data.token});
                        this.$store.commit('auth/setCompanies', {companies: res.data.companies});

                        this.$router.push({name: 'dashboard.main'});
                    })
                    .catch(error => {
                        switch (error.response ? error.response.status : error.code) {
                            case 'ECONNABORTED':
                                this.$noty.error("Мы не получили ответа от сервера.", {
                                    theme: 'metroui',
                                    timeout: 4000,
                                });

                                break;
                            case 400:
                                const errors = error.response.data.errors ? error.response.data.errors : error.response.data;
                                let compiled = '';

                                if (errors) {
                                    for (let err in errors) {
                                        compiled += ` ${err}: ${errors[err]}`;
                                    }
                                }

                                this.$noty.error(`Данные для входа не верны.${compiled}`, {
                                    theme: 'metroui',
                                    timeout: 4000,
                                });

                                break;
                            case 404:
                                this.$noty.error("Пользователь с такими данными не найден.", {
                                    theme: 'metroui',
                                    timeout: 4000,
                                });

                                break;
                            case 422:
                                this.$noty.error("Неверный пароль или ваш аккаунт деактивирован.", {
                                    theme: 'metroui',
                                    timeout: 4000,
                                });

                                break;
                            default:
                                this.$noty.error("Неизвестная ошибка сервера.", {
                                    theme: 'metroui',
                                    timeout: 4000,
                                });
                        }

                        return error.response ? error.response.statusText : error.code;
                    })
                    .finally(() => {
                        this.checkin = false;
                    });
            },
            preventLogin() {
                return !this.checkin;
            }
        },
        computed: {
            modalState: {
                get() {
                    return this.dialog;
                },
                set(value) {
                    this.$bus.$emit('get-face-login-modal-state', value);
                }
            }
        }
    }
</script>

<style scoped>
    .dialog-header, .dialog-header * {
        font-family: 'Proxima Nova', sans-serif;
    }

    .v-card__title {
        padding-bottom: 0px;
    }

    .bff {
        font-weight: 900;
    }

    .input-shadow label {
        font-weight: 500;
    }

    .input-shadow .v-input__slot {
        box-shadow: 0 2px 4px -1px rgba(0, 0, 0, .2), 0 4px 5px 0 rgba(0, 0, 0, .14), 0 1px 10px 0 rgba(0, 0, 0, .12) !important;
    }

    .v-text-field > .v-input__control > .v-input__slot:after, .v-text-field > .v-input__control > .v-input__slot:before {
        width: 0 !important;
    }
</style>