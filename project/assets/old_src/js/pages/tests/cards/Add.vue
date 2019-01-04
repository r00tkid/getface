<template>
    <v-container fluid>
        <v-form>
            <v-container>

                <v-layout row wrap>
                    <v-flex xs12>
                        <v-text-field
                                v-model="cardAmount"
                                v-on:input="intPurify"
                                outline
                                label="Amount"
                                type="number"
                                class="remove-number-arrows"
                        >
                            <v-btn
                                    slot="append-outer"
                                    style="top: -12px"
                                    color="accent darken-1"
                            >Generate
                            </v-btn>
                        </v-text-field>
                    </v-flex>

                </v-layout>
            </v-container>
        </v-form>

        <v-container>

        </v-container>
    </v-container>
</template>

<script>
    export default {
        name: "add",
        data() {
            return {
                cardGetterAlias: this.$store.getters['tests/cards/getCard'],
                cardAmount: 0,
            }
        },
        methods: {
            getCard(uuid) {
                this.cardGetterAlias(uuid);
            },
            setCard(card) {
                this.$store.$emit('tests/cards/setCard', card);
            },
            makeRandomCards() {

            },
            intPurify() {
                this.cardAmount = parseInt(this.cardAmount);
            }
        }
    }
</script>