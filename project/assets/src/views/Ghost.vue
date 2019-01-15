<template>
    <v-container fluid>
        <abn-ghost></abn-ghost>
    </v-container>
</template>

<script>
    export default {
        name: "ghost",
        components: {
            "abn-ghost": () => import('./../components/modals/ghost-modal/ExampleGhostModal')
        }
    }
</script>
