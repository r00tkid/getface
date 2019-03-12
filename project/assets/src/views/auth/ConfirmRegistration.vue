<template>
    <v-container fluid>
        <v-layout justify-center>
            <div class="abn-time-out-handler">
                <p id="main_text">Подождите. Идёт проверка ваших регистрационных данных. Страница сама перезагрузится
                    через
                    <span>{{ getCurrentSecond }}</span> секунд...
                </p>
            </div>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: "confirm-registration",
        mounted() {
            let timer = setTimeout(registrationTimer, 1000, this);

            function registrationTimer(instance) {
                if (instance.getCurrentSecond !== 1) {
                    instance.timer -= 1;

                    timer = setTimeout(registrationTimer, 1000, instance);
                } else instance.sendActivation();
            }
        },
        data() {
            return {
                user_id: Number(this.$route.params.id),
                user_key: this.$route.params.activation,
                timer: 10,
            };
        },
        computed: {
            getCurrentSecond() {
                return this.timer;
            }
        },
        methods: {
            sendActivation() {
                this.$http("auth.confirmation", window.collections.collectObject(this.$data, 'user_id', 'user_key'), "post")
                    .then(res => {
                        this.$store.commit('auth/setToken', {token: res.data.token});
                        this.$store.commit('auth/setCompanies', {companies: res.data.companies});

                        this.$router.push({name: 'dashboard.main'});
                    })
                    .catch(e => {
                        e = e.response;

                        switch (e.status) {
                            case 404:
                                this.activationNotFound();

                                break;
                            case 409:
                                if (e.data.active) {
                                    this.activationAlreadyActivated();
                                } else {
                                    this.activationKeyProblem();
                                }

                                break;
                            case 500:
                                this.activationServerFault();

                                break;
                            default:
                                this.activationUnknown();
                        }
                    });
            },
            activationAlreadyActivated() {
                document.querySelector("#main_text").innerHTML = "Этот аккаунт уже активирован. Воспользуйтесь формой входа, пожалуйста.";

                setTimeout(function (vue) {
                    vue.$bus.$emit("get-face-login-modal");
                }, 1500, this);
            },
            activationUnknown() {
                document.querySelector("#main_text").innerHTML = "Неизвестная ошибка сервера. Обратитесь к администрации.";
            },
            activationKeyProblem() {
                document.querySelector("#main_text").innerHTML = "Похоже, что секретный ключ активации повреждён.<br>Отправляем новый.";

                this.resendMailInvitation(this.user_id);
            },
            activationNotFound() {
                document.querySelector("#main_text").innerHTML = "Данный аккаунт не был найден в системе. Возможно вы не прошли регистрацию?";

                setTimeout(function (vue) {
                    vue.$bus.$emit("get-face-register-modal");
                }, 2000, this);
            },
            activationServerFault() {
                document.querySelector("#main_text").innerHTML = "Сервер временно не доступен. Повторите попытку активации позже или обратитесь к администрации.";
            },
            resendMailInvitation(user_id) {
                this.$http('auth.resend', {user_id: user_id}, 'post')
                    .then(res => {
                        this.$noty.info("На вашу почту были высланы обновлённые данные для активации.", {
                            theme: 'bootstrap-v4',
                            timeout: 9000,
                        });
                    })
                    .catch(e => {
                        const res = e.response;

                        switch (res.status) {
                            case 404:
                                this.$noty.error("Аккаунт не найден. Обновление активации отменено.", {
                                    theme: 'metroui',
                                    timeout: 3000,
                                });

                                break;
                            case 406:
                                this.$noty.error("В ваших данных были найдены ошибки. Обратитесь к администрации.", {
                                    theme: 'metroui',
                                    timeout: 3000,
                                });

                                break;
                            case 409:
                                if (res.data.active) {
                                    this.$noty.error("Аккаунт уже активирован. Попробуйте воспользоваться формой восстановления пароля.", {
                                        theme: 'metroui',
                                        timeout: 3000,
                                    });

                                    return;
                                }

                                this.$noty.error("С вашим аккаунтом что-то не так. Пожалуйста, свяжитесь с тех поддержкой для разъяснения ситуации.");

                                break;
                            default:
                                this.$noty.error(res.data.detail ? res.data.detail : "Ошибка сервера.");
                        }
                    });
            },
        },
    }
</script>

<style scoped>
    .abn-time-out-handler {
        font-family: "Proxima Nova", sans-serif;
        position: fixed;
        top: 50%;
        transform: translateY(-50%);
    }

    .abn-time-out-handler span {
        font-size: 1.9rem;
        color: #ff7f50;
    }

    #main_text {
        font-size: 1.3rem;
        text-align: center;
    }
</style>
