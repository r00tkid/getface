<template>
    <v-layout row justify-center>
        <v-dialog v-model="dialog" max-width="450px">
            <v-card>
                <v-card-text>
                    <v-container grid-list-md>
                        <v-layout wrap align-center>
                            <v-flex xs12 class="text-xs-center dialog-header">
                                <span class="subheading bff">ВОССТАНОВИТЬ ПАРОЛЬ</span>
                                <v-card-title class="justify-center">
                                    <span class="subheading">ВОЙТИ С ПОМОЩЬЮ</span>
                                </v-card-title>
                                <v-flex xs12>
                                    <v-text-field label="Email указанный при регистрации"
                                                  required></v-text-field>
                                </v-flex>
                                <v-flex xs12>
                                    <p>I'm not a robot, I swear</p>
                                </v-flex>
                                <v-flex xs12 d-flex justify-center>
                                    <vue-recaptcha sitekey="6LcFAYkUAAAAAEmjE31ouF7BR3fSumdWgeYDURhO" type="flag">
                                    </vue-recaptcha>

                                </v-flex>
                                <v-flex xs12 d-flex>
                                    <v-btn :disabled="btnDisabled" color="purple lighten-2" class="white--text">ВОССТАНОВИТЬ</v-btn>
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
        components: { VueRecaptcha },
        data: () => ({
            btnDisabled: false,
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
        beforeCreate() {
            $bus.$emit('pidoras', { a: 1 });

            $bus.$on('pidoras', (...shit) => {
                console.log(shit);
            });

            $bus.$on('verify', function (...shit) {
                console.log(shit);
            });
        },
        mounted() {
            let recaptchaScript = document.createElement('script')
            recaptchaScript.setAttribute('src', 'https://www.google.com/recaptcha/api.js?onload=vueRecaptchaApiLoaded&render=explicit')
            recaptchaScript.setAttribute('async', 'true')
            recaptchaScript.setAttribute('defer', 'true')
            document.head.appendChild(recaptchaScript)
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