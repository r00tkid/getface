<template>
    <v-container fluid>
        <v-layout justify-center>
            <p>{{ user_id }}</p>
            <p>{{ user_key }}</p>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: "confirm-registration",
        data() {
            return {
                confirm_terms: false,
                user_id: Number(this.$route.params.id),
                user_key: this.$route.params.activation,
            };
        },
    }
</script>