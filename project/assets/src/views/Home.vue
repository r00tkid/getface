<template>
    <v-container>
        <v-layout align-center justify-center row>
            <v-flex fill-height class="main-field pa-5">
                <h1>Hell yeah</h1>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<style scoped>
    .main-field {
        background-color: #fff;
        height: 80vh;
        border: #d4d4d4 solid 1px;
        border-radius: 8px;
    }
</style>
<script>
    export default {
        name: "abn-home",
        head: {
            title() {
                return {
                    inner: 'Home',
                }
            },
        },
    }
</script>