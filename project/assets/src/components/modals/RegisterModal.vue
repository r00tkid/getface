<template>
    <v-layout row justify-center>
        <v-dialog v-model="dialog" persistent max-width="500px">
            <v-card>
                <!--Steppers ahead!-->
                <!--Header is hidden anyway-->
                <v-stepper v-model="e1">
                    <v-stepper-header class="hide-header">
                        <v-stepper-step :complete="e1 > 1" step="1">Basic data</v-stepper-step>
                        <v-divider></v-divider>
                        <v-stepper-step :complete="e1 > 2" step="2">Peronsl data</v-stepper-step>
                        <v-divider></v-divider>
                    </v-stepper-header>

                    <v-stepper-items class="input-shadow">
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
                                                    box
                                                    background-color="white"
                                                    @keydown.space.prevent
                                                    @keyup.enter.prevent="$refs.step1Username.focus()"
                                                    v-model="email"
                                                    ref="step1Email"
                                                    color="purple" prepend-inner-icon="email" label="Ваш Email"
                                                    required
                                                    :rules="emailRules"
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    box
                                                    background-color="white"
                                                    v-model="username"
                                                    ref="step1Username"
                                                    @keyup.enter.prevent="$refs.step1Password.focus()"
                                                    color="purple" prepend-inner-icon="account_circle"
                                                    label="Имя пользователя"
                                                    required
                                                    :rules="usernameRules"
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    box
                                                    background-color="white"
                                                    v-model="password"
                                                    ref="step1Password"
                                                    @keyup.enter.prevent="$refs.step1PasswordConfirm.focus()"
                                                    color="purple" prepend-inner-icon="vpn_key" label="Пароль"
                                                    type="password"
                                                    required
                                                    :rules="passwordRules"
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    box
                                                    background-color="white"
                                                    v-model="password_confirmation"
                                                    ref="step1PasswordConfirm"
                                                    @keyup.enter.prevent="nextStep(step1Valid)"
                                                    color="purple" prepend-inner-icon="vpn_key" label="Повторите пароль"
                                                    type="password"
                                                    required
                                                    :rules="passwordConfirmation"
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12 d-flex>
                                            <v-btn @click.prevent="e1=2" :disabled="!step1Valid"
                                                   color="primary lighten-2" class="white--text"
                                            >
                                                ДАЛЕЕ
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
                                                    box
                                                    background-color="white"
                                                    v-model="first_name"
                                                    ref="step2FirstName"
                                                    @keyup.enter.prevent="$refs.step2LastName.focus()"
                                                    :rules="step2FirstRule"
                                                    color="purple" label="Имя пользователя"
                                                    required
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    box
                                                    background-color="white"
                                                    v-model="last_name"
                                                    @keyup.enter.prevent="$refs.step2Phone.focus()"
                                                    ref="step2LastName"
                                                    :rules="step2LastRule"
                                                    color="purple" label="Фамилия пользователя"
                                                    required
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    box
                                                    prefix="+"
                                                    background-color="white"
                                                    v-model="phone"
                                                    ref="step2Phone"
                                                    @keyup.enter.prevent="registerUser"
                                                    :rules="step2PhoneRule"
                                                    mask="#####################"
                                                    color="purple" label="Телефон"
                                                    required
                                            ></v-text-field>
                                        </v-flex>


                                        <v-flex xs12 d-flex>
                                            <v-btn @click.prevent="e1=1" color="white lighten-2">
                                                НАЗАД
                                            </v-btn>
                                            <v-btn @click.prevent="registerUser" :disabled="!step2Valid"
                                                   color="primary lighten-2" class="white--text"
                                            >
                                                ЗАРЕГИСТРИРОВАТЬСЯ
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
                                                    box
                                                    background-color="white"
                                                    :rules="step3NameRule"
                                                    ref="step3Name"
                                                    v-model="company_name"
                                                    color="purple" label="Название компании"
                                                    required
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    box
                                                    background-color="white"
                                                    :rules="step3AdressRule"
                                                    ref="step3Adress"
                                                    clearable
                                                    v-model="company_address"
                                                    color="purple" label="Адресс компании"
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    box
                                                    background-color="white"
                                                    :rules="step3PhoneRule"
                                                    ref="step3Phone"
                                                    type="phone"
                                                    v-model="company_phone"
                                                    clearable
                                                    color="purple" label="Телефон компании"
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs12>
                                            <v-text-field
                                                    box
                                                    background-color="white"
                                                    :rules="step3PhoneRule"
                                                    ref="step3Email"
                                                    @keydown.space.prevent
                                                    v-model="company_email"
                                                    color="purple" label="Email компании"
                                                    required
                                            ></v-text-field>
                                        </v-flex>

                                        <v-flex xs12 d-flex>
                                            <v-btn to="dashboard" color="white lighten-2">
                                                Пропустить
                                            </v-btn>
                                            <v-btn @click.prevent="registerCompany" :disabled="!step3Valid"
                                                   color="primary lighten-2" class="white--text"
                                            >
                                                ДОБАВИТЬ
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
                checkin: false,
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
                phone: '',
                emailRules: [
                    v => !!v || 'Обязательное поле',
                    v => v.length >= 6 || 'Email слишком короткий',
                    v => /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(v) || 'Неправильный email'
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
                step2PhoneRule: [
                    v => !!v || 'Обязательное поле',
                ],
                step3NameRule: [
                    v => !!v || 'Обязательное поле',
                    v =>  v.length >= 3 || 'Название слишком короткое'
                ],
                step3PhoneRule: [
                    v => (v.length == 0 || v.length >= 6 ) || 'Телефон слишком короткий'
                ],
                step3AdressRule: [
                    v => (v.length == 0 || v.length >= 5 ) || 'Адресс слишком короткий'
                ],
                step3EmailRule: [
                    v => !!v || 'Обязательное поле',
                    v => v.length >= 6 || 'Email слишком короткий',
                    v => /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(v) || 'Неправильный email'
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
            nextStep(step) {
                if (step)
                    this.e1++;
            },
            registerUser() {
                if (!this.step2Valid)
                    return false;
                this.checkin = true;

                let vueData = Object.assign({}, this.$data);
                let data = _.pick(vueData, [
                    'username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name', 'phone'
                ])
                this.$store.dispatch('auth/register', data).then(() => {
                    // this.$router.push('dashboard');
                    this.e1 = 3;
                }).catch(error => {
                    let errors = error.response.data.errors
                    let resp = [];
                    for (let err in errors) {
                        resp.push(err + ': ' + errors[err].join(', '));
                    }
                    let noty = this.$noty.error("Упс, кажется неправильные данные для входа: <br>" + resp.join("<br>"), {
                        theme: 'metroui',
                    });
                    // setTimeout(() => this.notifi.close(), 2000);
                    this.e1 = 1;
                }).finally(() => {
                    this.checkin = false;
                })
            },
            registerCompany() {
                if (!this.step3Valid)
                    return false;

                let vueData = Object.assign({}, this.$data);
                let data = {
                    name: this.company_name,
                    email: this.company_email,
                    address: this.company_address || null,
                    phone: this.company_phone || null,
                }

                // let data = _.pick(vueData, [
                //     'company_name', 'company_address', 'company_phone', 'company_email'
                // ]);
                // Request
                this.axios.request({
                    method: 'POST',
                    url: 'company',
                    data: data
                }).then(res => {
                    let noty = this.$noty.success(res.data.detail, {
                        theme: 'metroui',
                    });
                    setTimeout(() => {
                        noty.close();
                        this.$router.push('dashboard');
                    }, 2000);
                }).catch(e => {
                    let noty = this.$noty.error(e.message, {
                        theme: 'metroui',
                    });
                    setTimeout(() => noty.close(), 2000);
                });
            }
        },
        updated() {
            this.step1Valid = (this.$refs.step1Email.validate()
                && this.$refs.step1Password.validate()
                && this.$refs.step1Username.validate()
                && this.$refs.step1PasswordConfirm.validate());

            this.step2Valid = (this.$refs.step2FirstName.validate()
                && this.$refs.step2LastName.validate()
                && this.$refs.step2Phone.validate());

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