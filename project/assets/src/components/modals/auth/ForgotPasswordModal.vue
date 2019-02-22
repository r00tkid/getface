<template>
    <v-layout row justify-center :if="dialog">
        <v-dialog v-model="modalState" max-width="450px" @keydown.esc="modalState = false">
            <v-card>
                <v-card-text>
                    <v-container grid-list-md>
                        <v-layout wrap align-center>
                            <v-flex xs12 class="text-xs-center dialog-header">

                                <span class="subheading bff">ВОССТАНОВИТЬ ПАРОЛЬ</span>
                                <v-flex xs12>
                                    <v-text-field label="Email указанный при регистрации"
                                                  color="purple"
                                                  class="mt-3"
                                                  solo
                                                  v-model="email"
                                                  @keyup.enter="submitPasswordReset"
                                                  required>
                                    </v-text-field>
                                </v-flex>

                                <v-flex d-flex justify-center :if="'development' !== projectMode">
                                    <v-layout justify-center>
                                        <vue-recaptcha @verify="enableButton"
                                                       @expired="retry"
                                                       sitekey="6LcFAYkUAAAAAEmjE31ouF7BR3fSumdWgeYDURhO" type="flag">
                                        </vue-recaptcha>
                                    </v-layout>
                                </v-flex>

                                <v-flex xs12 d-flex>
                                    <v-btn @click.prevent="submitPasswordReset"
                                           :disabled="'development' !== projectMode ? btnDisabled : (btnDisabled = false)"
                                           color="primary lighten-2"
                                           class="white--text">
                                        ВОССТАНОВИТЬ
                                    </v-btn>
                                </v-flex>

                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-card-text>
            </v-card>
        </v-dialog>
    </v-layout>
</template>

<script>
    import VueRecaptcha from 'vue-recaptcha';

    export default {
        name: "get-face-forgot-password",
        components: {VueRecaptcha},
        props: {
            dialog: {
                type: Boolean,
                default: false,
            },
        },
        data: () => ({
            btnDisabled: true,
            email: '',
            projectMode: process.env.NODE_ENV,
        }),
        computed: {
            modalState: {
                get() {
                    return this.dialog;
                },
                set(value) {
                    this.$bus.$emit('get-face-forgot-password-modal-state', value);
                },
            }
        },
        beforeMount() {
            this.$bus.$on('get-face-forgot-password-modal', this.checkEventPayload);
        },
        mounted() {
            if ('development' !== this.projectMode) {
                // ReCaptcha script mount
                let recaptchaScript = document.createElement('script');
                recaptchaScript.setAttribute('id', 're-captcha-script');
                recaptchaScript.setAttribute('src', 'https://www.google.com/recaptcha/api.js?onload=vueRecaptchaApiLoaded&render=explicit');
                recaptchaScript.setAttribute('async', 'true');
                recaptchaScript.setAttribute('defer', 'true');
                document.head.appendChild(recaptchaScript);
            }
        },
        beforeDestroy() {
            if ('development' !== this.projectMode) {
                // ReCaptcha script unmount
                let captcha = document.head.querySelector('#re-captcha-script');
                captcha && captcha.parentNode.removeChild(captcha);

                let re_captcha = document.head.querySelector("[src*='recaptcha']");
                re_captcha && re_captcha.parentNode.removeChild(re_captcha);
            }
        },
        methods: {
            enableButton() {
                this.btnDisabled = false;
            },
            retry() {
                this.btnDisabled = true;
            },
            checkEventPayload(payload) {
                if (payload && payload.email) {
                    this.email = payload.email;
                }
            },
            submitPasswordReset() {
                if (this.btnDisabled) {
                    return;
                }

                this.$http('auth.password_restore', {email: this.email}, 'post')
                    .then(res => {
                        this.$noty.success('Инструкции по восстановлению пароля высланы на почту.', {
                            theme: 'metroui',
                            timeout: 2000,
                        });

                        this.modalState = false;
                    })
                    .catch(err => {
                        switch (err.response ? err.response.status : err.code) {
                            case 404:
                                this.$noty.error('Пользователь с такими данными не найден.', {
                                    theme: 'metroui',
                                    timeout: 2000,
                                });

                                break;
                            case 409:
                                this.$noty.error('Пользователь с такими данными не найден или аккаунт не активирован.', {
                                    theme: 'metroui',
                                    timeout: 2000,
                                });

                                break;
                            default:
                                this.$noty.error('Неизвестная ошибка сервера.', {
                                    theme: 'metroui',
                                    timeout: 2000,
                                });
                        }
                    });
            },
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
</style>