<template>
    <div>
        <p>{{ user_id }}</p>
        <p>{{ user_key }}</p>
    </div>
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

<style scoped>

</style>