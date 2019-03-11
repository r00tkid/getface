<template>
    <v-btn large class="mr-5" icon @click="addMessage">
        <v-badge color="green"
                 :value="messages > 0"
                 overlap
                 left>
            <template slot="badge">
                <span v-text="messages"></span>
            </template>
            <v-icon color="grey lighten-1" large>
                notification_important
            </v-icon>
        </v-badge>
    </v-btn>
</template>

<script>
    export default {
        name: "get-face-header-notifications",
        data() {
            return {
                messages: 0,
            };
        },
        methods: {
            addMessage() {
                this.messages++;
            },
        },
    }
</script>
