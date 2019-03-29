<template>
    <v-dialog v-model="modalState" @keydown.esc="modalState = false" max-width="400px" class="dialog-holder">
        <v-card>
            <v-card-title primary-title>
                <div class="flex text-xs-center">
                    <div class="headline">Тариф для "{{ company && company.name ? company.name : '' }}"</div>
                </div>
            </v-card-title>

            <v-card-text>
                <v-autocomplete
                        v-model="checked_rate"
                        :items="rates"
                        label="Выбрать тариф"
                        item-text="name"
                        hint="@test"
                        auto-select-first
                        persistent-hint
                        return-object
                        outline
                >
                </v-autocomplete>
            </v-card-text>

            <v-card-actions class="right-buttons">
                <v-btn flat icon color="indigo" @click="getAvailableRates">
                    <v-icon>refresh</v-icon>
                </v-btn>

                <v-spacer><!-- 'pull' btns right --></v-spacer>

                <v-btn flat color="error darken" @click="closeAndClear">Отмена</v-btn>
                <v-btn flat color="success darken" :disabled="disablePayButton" @click="payForRate">Принять</v-btn>
            </v-card-actions>
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
                checked_rate: null,
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
            },
            disablePayButton: {
                get() {
                    if (this.company && this.company.time_left > 0) return true;

                    return !this.checked_rate;
                },
            }
        },
        watch: {
            company(new_value, old_value) {
                if (this.rates) {
                    this.available_rates = this.rates;
                } else {
                    this.getAvailableRates();
                }
            },
        },
        methods: {
            closeAndClear() {
                this.modalState = false;
                this.checked_rate = null;
            },
            setDefaultRates() {
                this.available_rates = {name: "Нет данных по тарифам", id: 0, per_month: 0, lifetime: 0}
            },
            getAvailableRates(with_notify = false) {
                this.$http("company.rate.available")
                    .then(res => {
                        res.data && res.data.rates && this.setFetchedRates(res.data.rates);

                        if (with_notify) {
                            // with_notify there - mouse event if called on @click event (nothing suspicious)
                            this.$noty.success("Тарифы успешно обновлены", {
                                theme: "bootstrap-v4",
                                timeout: 1000,
                            });
                        }
                    })
                    .catch(err => {
                        const state = err.response.status || err.status;

                        switch (state) {
                            case 404:
                                this.$noty.warning("Тарифы не были найдены", {
                                    theme: "bootstrap-v4",
                                    timeout: 2000,
                                });

                                break;
                            case 403:
                                this.$noty.error("Недостаточно прав", {
                                    theme: "bootstrap-v4",
                                    timeout: 2000,
                                });

                                break;
                            case 500:
                                this.$noty.error("Ошибка сервера (500)", {
                                    theme: "bootstrap-v4",
                                    timeout: 2000,
                                });

                                break;
                            default:
                                this.$noty.error(`Неизвестная ошибка: ${state}`, {
                                    theme: "bootstrap-v4",
                                    timeout: 2000,
                                });
                        }
                    });
            },
            payForRate() {
                this.$http("company.rate.buy", {
                    company_id: this.company.id,
                    rate_id: this.checked_rate.id,
                }, "post")
                    .then(res => {
                        if (res && res.data.company) {
                            this.setCurrentCompany(res.data.company);

                            this.closeAndClear();

                            this.$noty.success("Оплата прошла успешно", {
                                theme: "bootstrap-v4",
                                timeout: 2500,
                            });
                        }
                    })
                    .catch(err => {
                        const state = err.response.status || err.status;

                        switch (state) {
                            case 409:
                                this.$noty.warning("Компания уже имеет тариф", {
                                    theme: "bootstrap-v4",
                                    timeout: 2000,
                                });

                                break;
                            case 404:
                                let type = err.response.data.detail.contains('company') ? 'Компания не найдена' : 'Тариф не найден';

                                this.$noty.warning(type, {
                                    theme: "bootstrap-v4",
                                    timeout: 2000,
                                });

                                break;
                            case 403:
                                this.$noty.error("Недостаточно прав", {
                                    theme: "bootstrap-v4",
                                    timeout: 2000,
                                });

                                break;
                            case 500:
                                this.$noty.error("Ошибка сервера (500)", {
                                    theme: "bootstrap-v4",
                                    timeout: 2000,
                                });

                                break;
                            default:
                                this.$noty.error(`Неизвестная ошибка: ${state}`, {
                                    theme: "bootstrap-v4",
                                    timeout: 2000,
                                });
                        }
                    })
            },
            ...mapMutations([
                'setFetchedRates',
                'setCurrentCompany',
            ]),
        },
    }
</script>

<style scoped>
    .dialog-holder {
        font-family: 'Proxima Nova', sans-serif;
    }
</style>