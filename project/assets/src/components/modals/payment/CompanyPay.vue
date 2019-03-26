<template>
    <v-dialog v-model="modalState" @keydown.esc="modalState = false" max-width="450px" class="dialog-holder">
        <v-card>
            <v-card-text>
                <v-container grid-list-md>
                    <v-layout wrap align-center>
                        <v-flex xs12 class="text-xs-center dialog-header">

                            <span class="subheading bff">Выберите тариф для "{{ company && company.name ? company.name : '' }}"</span>

                        </v-flex>
                    </v-layout>
                </v-container>
            </v-card-text>
        </v-card>
    </v-dialog>
</template>

<script>
    import {createNamespacedHelpers} from 'vuex';

    const {mapState, mapMutations} = createNamespacedHelpers('auth');

    export default {
        name: "get-face-company-pay",
        props: {
            modal_state: {
                type: Boolean,
                default: false,
            },
            parent: {
                type: Function,
                default: undefined,
            },
        },
        data() {
            return {
                projectMode: process.env.NODE_ENV,
                available_rates: null,
            }
        },
        computed: {
            ...mapState({
                company: state => state.current_company,
                rates: state => state.last_fetched_rates,
            }),
            modalState: {
                get() {
                    return this.modal_state;
                },
                set(state) {
                    this.parent().modal_state = state;
                }
            }
        },
        watch: {
            company(new_value, old_value) {
                if (this.rates) {
                    this.available_rates = this.rates;
                } else {
                    this.getAvailableRates();
                }

                new_value === old_value && this.$log("same");
            },
        },
        methods: {
            setDefaultRates() {
                this.available_rates = {name: "Нет данных по тарифам", id: 0, per_month: 0, lifetime: 0}
            },
            getAvailableRates() {
                const that = this;

                // asking for rates from server side
                this.$http("company.rates")
                    .then(res => {
                        res.data && res.data.rates && that.setFetchedRates(res.data.rates) || that.setDefaultRates();
                    })
                    .catch(err => {
                        const state = err.response.status || err.status;

                        switch (state) {
                            case 404:
                                that.$log("Achtung, not found");
                                break;
                            case 403:
                                that.$log("Achtung, no rights");
                                break;
                            case 500:
                                that.$log("Achtung, server fault");
                                break;
                            default:
                                that.$log("Achtung, unknown issue");
                        }
                    });
            },
            ...mapMutations([
                'setFetchedRates',
            ]),
        },
    }
</script>

<style scoped>
    .dialog-holder {
        font-family: 'Proxima Nova', sans-serif;
    }
</style>