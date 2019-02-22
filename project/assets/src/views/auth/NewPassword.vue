<template>
    <v-layout row justify-center :if="dialog">
        <v-card>
            <v-card-text>
                <v-container grid-list-md>
                    <v-layout wrap align-center>
                        <v-flex xs12 class="text-xs-center dialog-header">

                            <span class="subheading bff">Новый пароль</span>
                            <v-flex xs12>
                                <v-text-field label="Пароль"
                                              color="purple"
                                              class="mt-3"
                                              solo
                                              v-model="password"
                                              @keyup.enter="submitPasswordReset"
                                              required>
                                </v-text-field>
                            </v-flex>

                             <v-flex xs12>
                                <v-text-field label="Подтверждение пароля"
                                              color="purple"
                                              class="mt-3"
                                              solo
                                              v-model="password_confirmation"
                                              @keyup.enter="submitPasswordReset"
                                              required>
                                </v-text-field>
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
    </v-layout>
</template>

<script>
    export default {
        name: "NewPassword"
    }
</script>

<style scoped>

</style>