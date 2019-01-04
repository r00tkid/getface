<template>
    <v-footer :fixed="true" app class="abn-footer">
        <span>Abnormally &copy; {{ currentYear === 2018 ? currentYear : `2018 - ${currentYear}` }}</span>
    </v-footer>
</template>

<script>
    export default {
        name: "abn-footer",
        data: function () {
            return {
                currentYear: new Date().getFullYear(),
            };
        },
    }
</script>

<style scoped>
    .abn-footer {
        display: flex;
        flex-flow: row nowrap;
        justify-content: center;
        align-content: center;
    }
</style>