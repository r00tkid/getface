<template>
    <div class="employeeFaceId materialBox">
        <v-layout>
            <v-flex xs6>
                <v-avatar :size="150" color="grey lighten-4">
                    <img src="https://vuetifyjs.com/apple-touch-icon-180x180.png" alt="avatar">
                </v-avatar>
                <v-btn color="get-danger" dark class="removeID">Удалить Face ID</v-btn>
            </v-flex>
            <v-flex xs6>
                <v-layout align-center justify-space-around column fill-height>
                    <v-flex>
                        <v-select label="Solo field" solo></v-select>
                    </v-flex>
                    <v-flex>
                        <v-btn large color="primary" class="white--text">
                            Отправить
                            <br>логин и
                            пароль
                        </v-btn>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
    export default {};
</script>
