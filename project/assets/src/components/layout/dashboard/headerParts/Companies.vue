<template>
    <v-select
            v-if="companies && companies.length > 0"
            :disabled="companies.length === 1"
            v-model="current_id"
            :items="companies"
            item-value="id"
            item-text="name"
            hide-selected
            class="kill-select mt-1 get-face-nova minimal-width"
            solo
            flat
    ></v-select>
    <div v-else class="get-face-nova">
        <p class="text-xs-center align-self-center">Нет компаний</p>
    </div>
</template>

<script>
    import {createNamespacedHelpers} from 'vuex';

    const {mapState, mapMutations} = createNamespacedHelpers('auth');

    export default {
        name: "get-face-header-companies",
        data() {
            return {
                current_company_id: 0,
            };
        },
        mounted() {
            /* Mounted */
        },
        methods: {
            ...mapMutations([
                'setCurrentCompany'
            ]),
        },
        watch: {
            companies(companies) {
                if (companies && companies.length > 0 && this.current_company_id === 0) {
                    this.current_id = companies[0].id;
                }
            }
        },
        computed: {
            ...mapState({
                companies: state => state.companies,
            }),
            company: {
                get() {
                    const that = this;

                    try {
                        return this.companies[this.companies.findIndex(function (company) {
                            return that.current_company_id === company.id;
                        })];
                    } catch (e) {
                        return {id: 0};
                    }
                }
            },
            current_id: {
                get() {
                    return this.current_company_id;
                },
                set(company_id) {
                    this.current_company_id = company_id;

                    let company = null;

                    if (company_id && (company = this.company)) {
                        this.setCurrentCompany(company);

                        this.$bus.$emit("get-face-company-changed", company);
                    }
                },
            }
        },
    }
</script>

<style scoped>
    .get-face-nova {
        font-family: "Proxima Nova", sans-serif;
    }

    .minimal-width {
        min-width: 151px;
    }
</style>