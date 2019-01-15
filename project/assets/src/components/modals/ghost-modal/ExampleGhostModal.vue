<template>
    <v-app>
        <img src="./ghost.svg" ref="ghost_image" style="display: none">
        <object id="abn-ghost-svg" ref="ghost_object" rel="image/svg+xml" height="201px" width="201px">

        </object>
        <form>
            <fieldset>
                <legend>Mouth</legend>
                <v-btn color="warning" @click="defaultMouth">Default smile</v-btn>
                <v-btn color="warning" @click="openMouth">Little smile</v-btn>
                <v-btn color="warning" @click="wideOpenMouth">Wide open smile</v-btn>
            </fieldset>

            <fieldset>
                <legend>Eyes</legend>
                <v-btn color="error" @click="eyesDefault">Default eyes</v-btn>
                <v-text-field
                        v-model="positionEye"
                        type="number"
                        label="Outline"
                        single-line
                        outline
                        @change="eyesMove(positionEye)"
                ></v-text-field>
            </fieldset>

            <fieldset>
                <legend>Arms</legend>
                <v-btn color="success" @click="defaultHands">Default arms</v-btn>
                <v-btn color="success" @click="closeHands">Close arms</v-btn>
            </fieldset>
        </form>
    </v-app>
</template>

<script>
    export default {
        name: "abn-example-ghost-modal",
        data() {
            return {
                ghost: null,
                positionEye: 0,
            }
        },
        mounted() {
            this.ghost = this.$refs.ghost_object;
            this.ghost.setAttribute('data', this.$refs.ghost_image.getAttribute('src'));
        },
        methods: {
            getSvg(element) {
                return this.ghost.contentDocument.querySelector(element);
            },
            getEyes() {
                return {
                    right: this.getSvg('#pupil-right'),
                    left: this.getSvg('#pupil-left'),
                }
            },
            getHands() {
                return {
                    right: this.getSvg('#ghost-arm-right'),
                    left: this.getSvg('#ghost-arm-left'),
                }
            },
            defaultMouth() {
                this.getSvg('#mouth').setAttribute("d", "M 75,115 C 79,120 91,126 101,125 110,125 126,118 127,114 125,117 117,125 101,125 85,126 79,117 75,115 Z");
            },
            openMouth() {
                this.getSvg('#mouth').setAttribute("d", "M 75,115 C 79,110 92,119 101,119 110,119 123,111 127,114 131,117 118,131 102,132 87,132 73,121 75,115 Z");
            },
            wideOpenMouth() {
                this.getSvg('#mouth').setAttribute("d", "M 75,115 C 79,110 92,117 102,117 111,117 123,111 127,114 131,117 123,136 102,136 81,137 73,121 75,115 Z");
            },
            eyesDefault() {
                (function (eyes) {
                    eyes.right.setAttribute('cx', 84);
                    eyes.right.setAttribute('cy', 69);

                    eyes.left.setAttribute('cx', 120);
                    eyes.left.setAttribute('cy', 71);
                })(this.getEyes());
            },
            eyesMove(value = 0) {
                value = value / 2.25;

                (function (eyes) {
                    eyes.right.setAttribute('cx', 78 + value);
                    eyes.right.setAttribute('cy', 75);

                    eyes.left.setAttribute('cx', 113 + value);
                    eyes.left.setAttribute('cy', 76);
                })(this.getEyes());
            },
            defaultHands() {
                (function (hands) {
                    hands.right.setAttribute("d", "M 45,89 C 25,92 9,108 11,124 13,141 27,115 48,119");
                    hands.left.setAttribute("d", "M 155,88 C 191,90 194,114 192,125 191,137 172,109 155,116");
                })(this.getHands());
            },
            closeHands() {
                (function (hands) {
                    hands.right.setAttribute("d", "M 45,89 C 54,64 103,48 106,64 108,80 65,121 48,119");
                    hands.left.setAttribute("d", "M 155,88 C 145,68 105,51 103,62 102,74 123,117 155,116");
                })(this.getHands());
            },
        },
    }
</script>

<style scoped>
    fieldset {
        padding: .5rem;
    }

    fieldset legend {
        margin: auto auto;
    }
</style>
