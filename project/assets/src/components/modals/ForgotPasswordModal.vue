<template>
    <v-layout row justify-center>
        <v-dialog v-model="dialog" max-width="450px">
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
                                                  required></v-text-field>
                                </v-flex>

                                <v-flex d-flex justify-center>
                                    <v-layout justify-center>
                                        <vue-recaptcha @verify="enableButton"
                                                       @expired="retry"
                                                       sitekey="6LcFAYkUAAAAAEmjE31ouF7BR3fSumdWgeYDURhO" type="flag">
                                        </vue-recaptcha>
                                    </v-layout>

                                </v-flex>
                                <v-flex xs12 d-flex>
                                    <v-btn @click.prevent="submitPasswordReset"
                                           :disabled="btnDisabled" color="primary lighten-2" class="white--text">
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
        name: "ForgotPasswordModal",
        components: {VueRecaptcha},
        data: () => ({
            btnDisabled: true,
            email: ''
        }),
        computed: {
            dialog: {
                get() {
                    return this.$store.getters['modal/forgot'];
                },
                set(value) {
                    return this.$store.commit('modal/setForgotPasswordModal', value);
                }
            }
        },

        mounted() {
            // ReCaptcha script mount
            let recaptchaScript = document.createElement('script')
            recaptchaScript.setAttribute('src', 'https://www.google.com/recaptcha/api.js?onload=vueRecaptchaApiLoaded&render=explicit')
            recaptchaScript.setAttribute('async', 'true')
            recaptchaScript.setAttribute('defer', 'true')
            document.head.appendChild(recaptchaScript)
        },
        methods: {
            enableButton() {
                this.btnDisabled = false;
            },
            retry() {
                this.btnDisabled = true;
            },
            submitPasswordReset() {
                let email = this.email;
                // Do shit
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
</style>