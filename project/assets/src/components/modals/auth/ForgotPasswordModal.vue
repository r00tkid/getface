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

                                <v-flex xs12 d-flex>
                                    <v-btn @click.prevent="submitPasswordReset"
                                           :disabled="btnDisabled"
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
    export default {
        name: "get-face-forgot-password",
        props: {
            dialog: {
                type: Boolean,
                default: false,
            },
        },
        data: () => ({
            btnDisabled: false,
            email: '',
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
        methods: {
            checkEventPayload(payload) {
                if (payload && payload.email) {
                    this.email = payload.email;
                }
            },
            submitPasswordReset() {
                if (this.btnDisabled) {
                    return;
                }

                this.btnDisabled = true;

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
                    })
                    .finally(() => {
                        this.btnDisabled = false;
                    });
            },
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
</style>