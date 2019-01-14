<template>
    <v-layout row justify-center>
        <v-dialog v-model="dialog" persistent max-width="500px">
            <v-card>
                <!--<v-card-text>-->
                <!--<v-container grid-list-md>-->
                <!--<v-layout wrap>-->
                <!--<v-flex xs12 class="text-xs-center dialog-header">-->
                <!--<span class="subheading bff">РЕГИСТРАЦИЯ</span>-->
                <!--<v-card-title class="justify-center">-->
                <!--<span class="subheading">ВОЙТИ С ПОМОЩЬЮ</span>-->
                <!--</v-card-title>-->
                <!--</v-flex>-->
                <!--<v-flex xs12 class="justify-center mb-3">-->
                <!--<div class="text-xs-center">-->
                <!--<v-btn fab dark medium color="red darken-2">-->
                <!--<v-icon>fab fa-google-plus-g</v-icon>-->
                <!--</v-btn>-->
                <!--<v-btn fab dark medium color="blue">-->
                <!--<v-icon>fab fa-vk</v-icon>-->
                <!--</v-btn>-->
                <!--<v-btn fab dark medium color="blue darken-3">-->
                <!--<v-icon>fab fa-facebook-f</v-icon>-->
                <!--</v-btn>-->
                <!--<v-btn fab dark medium color="red">-->
                <!--<v-icon>fab fa-yandex</v-icon>-->
                <!--</v-btn>-->
                <!--<v-btn fab dark medium color="blue">-->
                <!--<v-icon color="orange" large>fas fa-at</v-icon>-->
                <!--</v-btn>-->
                <!--</div>-->
                <!--</v-flex>-->
                <!--<v-flex xs12>-->
                <!--<v-text-field-->
                <!--solo-->
                <!--v-model="email"-->
                <!--color="purple" prepend-icon="email" label="Ваш Email"-->
                <!--required-->
                <!--:rules="emailRules"-->
                <!--&gt;</v-text-field>-->
                <!--</v-flex>-->
                <!--<v-flex xs12>-->
                <!--<v-text-field-->
                <!--solo-->
                <!--v-model="username"-->
                <!--color="purple" prepend-icon="account_circle" label="Имя пользователя"-->
                <!--required-->
                <!--:rules="usernameRules"-->
                <!--&gt;</v-text-field>-->
                <!--</v-flex>-->
                <!--<v-flex xs12>-->
                <!--<v-text-field-->
                <!--solo-->
                <!--v-model="password"-->
                <!--color="purple" prepend-icon="vpn_key" label="Пароль" type="password"-->
                <!--required-->
                <!--:rules="passwordRules"-->
                <!--&gt;</v-text-field>-->
                <!--</v-flex>-->
                <!--<v-flex xs12>-->
                <!--<v-text-field-->
                <!--solo-->
                <!--v-model="password_confirmation"-->
                <!--color="purple" prepend-icon="vpn_key" label="Повторите пароль" type="password"-->
                <!--required-->
                <!--:rules="passwordConfirmation"-->
                <!--&gt;</v-text-field>-->
                <!--</v-flex>-->
                <!--<v-flex xs12 d-flex>-->
                <!--<v-btn @click.prevent="registerUser" color="purple lighten-2" class="white&#45;&#45;text">-->
                <!--ЗАРЕГИСТРАИРОВАТЬСЯ-->
                <!--</v-btn>-->
                <!--</v-flex>-->
                <!--<v-flex xs12 class="text-xs-center">-->
                <!--<router-link to="login">У меня уже есть аккаунт</router-link>-->
                <!--</v-flex>-->

                <!--<v-flex xs12 class="text-xs-center">-->
                <!--<p>Создавая аккаут, вы соглашаетесь с нашими <a>Правилами и условиями</a> и <a>Положением-->
                <!--о конфиденциальности</a>-->
                <!--</p>-->
                <!--</v-flex>-->
                <!--</v-layout>-->
                <!--</v-container>-->
                <!--</v-card-text>-->

                <v-stepper v-model="e1">
                    <v-stepper-header class="hide-header">
                        <v-stepper-step :complete="e1 > 1" step="1">Name of step 1</v-stepper-step>

                        <v-divider></v-divider>

                        <v-stepper-step :complete="e1 > 2" step="2">Name of step 2</v-stepper-step>

                        <v-divider></v-divider>

                    </v-stepper-header>

                    <v-stepper-items>
                        <v-stepper-content step="1">
                            <v-card-text>
                                <v-container grid-list-md>
                                    <v-layout wrap ref="step1" v-model="step1Valid" lazy-validation>
                                        <v-flex xs12 class="text-xs-center dialog-header">
                                            <span class="subheading bff">РЕГИСТРАЦИЯ</span>
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
                                            <v-text-field
                                                    solo
                                                    v-model="email"
                                                    ref="step1Email"
                                                    color="purple" prepend-icon="email" label="Ваш Email"
                                                    required
                                                    :rules="emailRules"
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    solo
                                                    v-model="username"
                                                    ref="step1Username"
                                                    color="purple" prepend-icon="account_circle"
                                                    label="Имя пользователя"
                                                    required
                                                    :rules="usernameRules"
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    solo
                                                    v-model="password"
                                                    ref="step1Password"
                                                    color="purple" prepend-icon="vpn_key" label="Пароль" type="password"
                                                    required
                                                    :rules="passwordRules"
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    solo
                                                    v-model="password_confirmation"
                                                    ref="step1PasswordConfirm"
                                                    color="purple" prepend-icon="vpn_key" label="Повторите пароль"
                                                    type="password"
                                                    required
                                                    :rules="passwordConfirmation"
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12 d-flex>
                                            <v-btn @click.prevent="e1=2" :disabled="!step1Valid"
                                                   color="purple lighten-2" class="white--text"
                                            >
                                                ЗАРЕГИСТРАИРОВАТЬСЯ
                                            </v-btn>
                                        </v-flex>
                                        <v-flex xs12 class="text-xs-center">
                                            <router-link to="login">У меня уже есть аккаунт</router-link>
                                        </v-flex>

                                        <v-flex xs12 class="text-xs-center">
                                            <p>Создавая аккаут, вы соглашаетесь с нашими <a>Правилами и условиями</a> и
                                                <a>Положением
                                                    о конфиденциальности</a>
                                            </p>
                                        </v-flex>
                                    </v-layout>
                                </v-container>
                            </v-card-text>
                        </v-stepper-content>
                        <v-stepper-content step="2">
                            <v-card-text>
                                <v-container grid-list-md>
                                    <v-layout wrap>
                                        <v-flex xs12 class="text-xs-center dialog-header mb-3">
                                            <span class="subheading bff">Добавить новую компанию</span>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    solo
                                                    v-model="first_name"
                                                    ref="step2FirstName"
                                                    :rules="step2FirstRule"
                                                    color="purple" label="Имя пользователя"
                                                    required
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    solo
                                                    v-model="last_name"
                                                    ref="step2LastName"
                                                    :rules="step2LastRule"
                                                    color="purple" label="Фамилия пользователя"
                                                    required
                                            ></v-text-field>
                                        </v-flex>


                                        <v-flex xs12 d-flex>
                                            <v-btn @click.prevent="e1=1" color="white lighten-2">
                                                НАЗАД
                                            </v-btn>
                                            <v-btn @click.prevent="e1=3" :disabled="!step2Valid"
                                                   color="purple lighten-2" class="white--text"
                                            >
                                                ДАЛЕЕ
                                            </v-btn>
                                        </v-flex>
                                        <v-flex xs12 class="text-xs-center">
                                            <router-link to="login">У меня уже есть аккаунт</router-link>
                                        </v-flex>

                                    </v-layout>
                                </v-container>
                            </v-card-text>
                        </v-stepper-content>
                        <v-stepper-content step="3">
                            <v-card-text>
                                <v-container grid-list-md>
                                    <v-layout wrap>
                                        <v-flex xs12 class="text-xs-center dialog-header mb-3">
                                            <span class="subheading bff">Добавить новую компанию</span>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    solo
                                                    :rules="step3NameRule"
                                                    ref="step3Name"
                                                    v-model="company_name"
                                                    color="purple" label="Название компании"
                                                    required
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    solo
                                                    :rules="step3AdressRule"
                                                    ref="step3Adress"
                                                    v-model="company_address"
                                                    color="purple" label="Адресс компании"
                                                    required
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    solo
                                                    :rules="step3PhoneRule"
                                                    ref="step3Phone"
                                                    v-model="company_phone"
                                                    color="purple" label="Телефон компании"
                                                    required
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    solo
                                                    :rules="step3PhoneRule"
                                                    ref="step3Email"
                                                    v-model="company_email"
                                                    color="purple" label="Email компании"
                                                    required
                                            ></v-text-field>
                                        </v-flex>

                                        <v-flex xs12 d-flex>
                                            <v-btn @click.prevent="e1=1" color="white lighten-2">
                                                НАЗАД
                                            </v-btn>
                                            <v-btn @click.prevent="registerUser" :disabled="!step3Valid"
                                                   color="purple lighten-2" class="white--text"
                                            >
                                                ЗАРЕГИСТРАИРОВАТЬСЯ
                                            </v-btn>
                                        </v-flex>
                                        <v-flex xs12 class="text-xs-center">
                                            <router-link to="login">У меня уже есть аккаунт</router-link>
                                        </v-flex>

                                    </v-layout>
                                </v-container>
                            </v-card-text>
                        </v-stepper-content>
                    </v-stepper-items>
                </v-stepper>
            </v-card>
        </v-dialog>
    </v-layout>
</template>

<script>
    export default {
        name: "RegisterModal",
        data() {
            return {
                e1: 0,
                step1Valid: false,
                step2Valid: false,
                step3Valid: false,
                checkbox1: false,
                email: '',
                password: '',
                password_confirmation: '',
                username: '',
                last_name: '',
                first_name: '',
                company_name: '',
                company_address: '',
                company_phone: '',
                company_email: '',
                emailRules: [
                    v => !!v || 'Обязательное поле',
                    v => v.length >= 6 || 'Email слишком короткий',
                    v => /.+@.+/.test(v) || 'Неправильный email'
                ],
                usernameRules: [
                    v => !!v || 'Обязательное поле',
                    v => v.length >= 6 || 'Имя пользователя слишком короткое',
                ],
                passwordRules: [
                    v => !!v || 'Обязательное поле',
                    v => v.length >= 6 || 'Пароль слишком короткий',
                    // v => /^(?=.*[A-Z].*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8}$/.test(v) || 'Password isn\'t strong enough',
                ],
                passwordConfirmation: [
                    v => !!v || 'Обязательное поле',
                    v => v == this.password || 'Пароли не совпадают',
                ],
                step2FirstRule: [
                    v => !!v || 'Обязательное поле',
                    v => v.length >= 3 || 'Имя слишком короткое'
                ],
                step2LastRule: [
                    v => !!v || 'Обязательное поле',
                    v => v.length >= 3 || 'Фамилия слишком короткое'
                ],
                step3NameRule: [
                    v => !!v || 'Обязательное поле',
                    v => v.length >= 3 || 'Название слишком короткое'
                ],
                step3PhoneRule: [
                    v => !!v || 'Обязательное поле',
                    v => v.length >= 3 || 'Телефон слишком короткий'

                ],
                step3AdressRule: [
                    v => !!v || 'Обязательное поле',
                    v => v.length >= 5 || 'Адресс слишком короткое'
                ],
                step3EmailRule: [
                    v => !!v || 'Обязательное поле',
                    v => v.length >= 6 || 'Email слишком короткий',
                    v => /.+@.+/.test(v) || 'Неправильный email'
                ],
            }
        },
        computed: {
            dialog: {
                get() {
                    return this.$store.getters['modal/register'];
                },
                set(value) {
                    return this.$store.commit('modal/setRegisterModal', value);
                }
            },

        },
        mounted() {
            setTimeout(() => this.$store.commit('modal/setRegisterModal', true), 600)
        },
        destroyed() {
            this.$store.commit('modal/setRegisterModal', false);
        },
        methods: {
            registerUser() {
                let data = {
                    email: this.email,
                    password: this.password,
                    username: this.username,
                    password_confirmation: this.password_confirmation,
                    last_name: this.last_name,
                    first_name: this.first_name,
                    company_name: this.company_name,
                    company_address: this.company_address,
                    company_phone: this.company_phone,
                    company_email: this.company_email
                }
                this.$store.dispatch('auth/register', data).then(res => {
                    console.log(res);
                })
            },
        },
        updated() {
            this.step1Valid = (this.$refs.step1Email.validate()
                && this.$refs.step1Password.validate()
                && this.$refs.step1Username.validate()
                && this.$refs.step1PasswordConfirm.validate());

            this.step2Valid = (this.$refs.step2FirstName.validate()
                && this.$refs.step2LastName.validate());

            this.step3Valid = (this.$refs.step3Phone.validate()
                && this.$refs.step3Name.validate()
                && this.$refs.step3Adress.validate()
                && this.$refs.step3Email.validate())
        }
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

    .hide-header {
        display: none;
    }
</style>