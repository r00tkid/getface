<template>
    <v-layout row justify-center>
        <v-dialog v-model="dialog" persistent max-width="500px">
            <v-card>
                <v-card-text>
                    <v-container grid-list-md>
                        <v-layout wrap>
                            <v-flex xs12 class="text-xs-center dialog-header">
                                <span class="subheading bff">РЕГИСТРАЦИЯ</span>
                                <v-card-title class="justify-center">
                                    <span class="subheading">ВОЙТИ С ПОМОЩЬЮ</span>
                                </v-card-title>
                            </v-flex>
                            <v-flex xs12 class="justify-center">
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
                                <v-text-field prepend-icon="fas fa-user" label="Ваш Email" required></v-text-field>
                            </v-flex>
                            <v-flex xs12>
                                <v-text-field prepend-icon="vpn_key" label="Пароль" type="password"
                                              required></v-text-field>
                            </v-flex>
                            <v-flex xs12 d-flex>
                                <v-btn color="purple lighten-2" class="white--text">ЗАРЕГИСТРАИРОВАТЬСЯ</v-btn>
                            </v-flex>
                            <v-flex xs12 class="text-xs-center">
                                <router-link to="login">У меня уже есть аккаунт</router-link>
                            </v-flex>

                            <v-flex xs12 class="text-xs-center">
                                <v-text>Создавая аккаут, вы соглашаетесь с нашими <a>Правилами и условиями</a> и <a>Положением
                                    о конфиденциальности</a></v-text>
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
        name: "RegisterModal",
        data: () => ({
            checkbox1: false
        }),
        computed: {
            dialog: {
                get() {
                    return this.$store.getters['modal/register'];
                },
                set(value) {
                    return this.$store.commit('modal/setRegisterModal', value);

                }
            }
        },
        mounted() {
            setTimeout(function () {
                this.$store.commit('modal/setRegisterModal', true);
            }.bind(this), 600)
        },
        destroyed() {
            this.$store.commit('modal/setRegisterModal', false);
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
</style>