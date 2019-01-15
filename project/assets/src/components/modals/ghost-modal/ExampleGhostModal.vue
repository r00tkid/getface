<template>
    <v-app>
        <img id="abn-ghost-svg" ref="ghost_image" src="./ghost.svg"/>
        <v-btn color="warning" @click="changeMouth">Smile</v-btn>
    </v-app>
</template>

<script>
    export default {
        name: "abn-example-ghost-modal",
        data() {
            return {
                ghost: null,
            }
        },
        mounted() {
            this.ghost = this.$refs.ghost_image;
            console.log(this.ghost);
        },
        methods: {
            changeMouth() {
                console.log(this.ghost.querySelector('#mouth'));
                this.ghost.querySelector('#mouth').setAttribute("d", "M 75,115 C 79,110 92,119 101,119 110,119 123,111 127,114 131,117 118,131 102,132 87,132 73,121 75,115 Z");
            },
        }
    }
</script>