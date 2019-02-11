<template>
    <v-layout row justify-center :if="dialog">
        <v-dialog v-model="modalState" max-width="500px">
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
                                <v-btn :loading="checkin" @click="submitCredentials" color="primary lighten-2"
                                       class="white--text"
                                >
                                    Войти
                                </v-btn>
                            </v-flex>
                            <v-flex xs6>
                                <v-checkbox label="Запомнить меня" color="purple" v-model="remember_me"></v-checkbox>
                            </v-flex>
                            <v-flex xs6 class="text-xs-right">
                                <a @click="openForgotPassModal">Забыли пароль?</a>
                            </v-flex>
                            <v-flex xs12 class="text-xs-center">
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
        name: "LoginModal",
        props: {
            dialog: {
                type: Boolean,
                default: false,
            }
        },
        data() {
            return {
                checkin: false,
                remember_me: false,
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

                const vueData = Object.assign({}, this.$data);
                let data = _.pick(vueData, ['username', 'password', 'remember_me']);

                this.$store.dispatch('auth/login', data)
                    .then((res) => {
                        this.$router.push('dashboard')
                    })
                    .catch(error => {
                        if (error.code === 'ECONNABORTED') {
                            this.$noty.error("Мы не получили ответа от сервера.", {
                                theme: 'metroui',
                                timeout: 4000,
                            });

                            return 'timeout';
                        }

                        let errors = error.response.data.errors || error.response.data;
                        let resp = [];
                        for (let err in errors) {
                            resp.push(err + ': ' + errors[err].join(', '));
                        }

                        this.$noty.error("Упс, кажется неправильные данные для входа: <br>" + resp.join("<br>"), {
                            theme: 'metroui',
                            timeout: 4000,
                        });
                    })
                    .finally(() => {
                        this.checkin = false;
                    });
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
        font-family: 'Montserrat', sans-serif;
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
        width: 0% !important;
    }
</style>