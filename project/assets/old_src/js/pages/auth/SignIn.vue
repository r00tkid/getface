<template>
    <v-container class="text-sm-center abn-width-fix">
        <v-card>
            <v-card-text>
                <v-container grid-list-md>

                    <v-form v-model="valid">
                        <v-text-field
                                v-on:keyup.enter="$refs.password_field.focus()"
                                v-model="email.value"
                                :rules="email.rules"
                                label="E-mail"
                                required
                                autofocus
                        ></v-text-field>
                        <v-text-field
                                ref="password_field"
                                v-on:keyup.enter="sendLogin"
                                v-model="password.value"
                                :rules="password.rules"
                                type="password"
                                label="Пароль"
                                required
                        ></v-text-field>
                    </v-form>

                </v-container>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="orange darken-2" flat @click.stop="sendLogin" :disabled="isDisabled">Войти</v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script>
    export default {
        name: "abn-sign-in",
        data() {
            return {
                valid: false,
                sending: false,
                emailValidate: this.$store.getters['tech/emailValidate'],
                url: this.$store.getters['api/url'],
                email: {
                    value: '',
                    rules: [
                        v => !!v || 'Адрес почты обязателен',
                        v => v.length <= 100 || 'Адрес почты не может быть более ста символов',
                        v => v.length >= 6 || 'Адрес почты не может быть менее шести символов',
                        v => this.emailValidate(v) || 'Введите валидный aдрес почты ',
                    ],
                },
                password: {
                    value: '',
                    rules: [
                        v => !!v || 'Пароль обязятелен',
                        v => v.length >= 6 || 'Пароль не может быть менее шести символов',
                        v => v.length <= 100 || 'Пароль не может быть более ста символов'
                    ],
                },
            };
        },
        head: {
            title() {
                return {
                    inner: 'Sign In'
                }
            },
            meta() {
                return [/* Do not use this one. It's really horrible. */]
            },
        },
        methods: {
            sendLogin() {
                if (this.isDisabled) return;
                this.sending = true;

                const data = {
                    email: this.email.value,
                    password: this.password.value,
                };

                const url = this.url('user.login');

                this.$http.post(url, data)
                    .then(response => {
                        this.$log('No errors');
                        this.$log(response);
                    })
                    .catch(error => {
                        this.$log(error.response ? error.response : error)
                    })
                    .finally(() => {
                        this.sending = false;
                    })
            },
        },
        computed: {
            isDisabled() {
                return !this.valid || this.sending;
            }
        },
    }
</script>

<style scoped>
    .abn-width-fix {
        max-width: 50rem;
    }
</style>