<template>
    <v-container fluid>
        <v-layout row justify-center>
            <v-card>
                <v-card-text>
                    <v-container grid-list-md>
                        <v-layout wrap align-center>
                            <v-form v-model="form_valid">
                                <v-flex xs12 class="text-xs-center dialog-header">

                                    <span class="subheading bff">Новый пароль</span>
                                    <v-flex xs12>
                                        <v-text-field label="Пароль"
                                                      :append-icon="show_pass ? 'visibility_off' : 'visibility'"
                                                      color="purple"
                                                      class="mt-3"
                                                      solo
                                                      v-model="password"
                                                      @keyup.enter="$refs.password_confirmation.focus()"
                                                      @click:append="show_pass = !show_pass"
                                                      :type="show_pass ? 'text' : 'password'"
                                                      :rules="[rules.required, rules.min]"
                                                      required>
                                        </v-text-field>
                                    </v-flex>

                                    <v-flex xs12>
                                        <v-text-field ref="password_confirmation"
                                                      :append-icon="show_pass ? 'visibility_off' : 'visibility'"
                                                      label="Подтверждение пароля"
                                                      color="purple"
                                                      class="mt-3"
                                                      solo
                                                      v-model="password_confirmation"
                                                      @keyup.enter="submitPasswordReset"
                                                      @click:append="show_pass = !show_pass"
                                                      :type="show_pass ? 'text' : 'password'"
                                                      :rules="[rules.required, rules.min, rules.match]"
                                                      required>
                                        </v-text-field>
                                    </v-flex>

                                    <v-flex xs12 d-flex>
                                        <v-btn @click="submitPasswordReset"
                                               :disabled="!canSend"
                                               color="primary lighten-2"
                                               class="white--text">
                                            Восстановить доступ
                                        </v-btn>
                                    </v-flex>

                                </v-flex>
                            </v-form>
                        </v-layout>
                    </v-container>
                </v-card-text>
            </v-card>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: "new-password",
        data() {
            return {
                user_id: Number(this.$route.params.id),
                user_key: this.$route.params.activation,
                password: '',
                password_confirmation: '',
                sending_prevent: false,
                show_pass: false,
                form_valid: false,
                rules: {
                    required: v => !!v || 'Обязательное поле',
                    min: v => v.length > 0 || 'Минимум шесть символов',
                    match: v => v === this.password || 'Пароли не совпадают',
                }
            };
        },
        mounted() {

        },
        methods: {
            submitPasswordReset() {
                if (!this.canSend) return;
                this.sending_prevent = true;

                this.$http('auth.password_reset', {
                    user_id: this.user_id,
                    user_key: this.user_key,
                    password: this.password,
                    password_confirmation: this.password_confirmation,
                }, 'post')
                    .then(res => {
                        this.$store.commit('auth/setToken', {token: res.data.token});
                        this.$store.commit('auth/setCompanies', {companies: res.data.companies});

                        this.$router.push({name: 'dashboard.main'});
                    })
                    .catch(err => {
                        this.$log(err.response);
                    })
                    .finally(() => setTimeout(function (component) {
                        // debounce
                        component.sending_prevent = false;
                    }, 777, this));
            },
        },
        computed: {
            canSend() {
                return !this.sending_prevent && this.form_valid;
            }
        }
    }
</script>