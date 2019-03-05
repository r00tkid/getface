<template>
    <v-select
            v-if="companies && companies.length > 0"
            :disabled="companies.length === 1"
            v-model="company_current"
            :items="companies"
            item-value="id"
            item-text="name"
            hide-selected
            class="kill-select mt-1 get-face-nova"
            solo
            flat
    ></v-select>
    <div v-else class="get-face-nova">
        <p class="text-xs-center align-self-center">Нет компаний</p>
    </div>
</template>

<script>
    export default {
        name: "get-face-companies",
        beforeMount() {
            this.$bus.$on('get-face-updated-companies', this.setCompanies);

            let counter = 3;

            function checkCompaniesUntilDone(vue) {
                if (--counter === 0) {
                    return; // To not disturb code too many times
                }

                if (vue.$store.getters["auth/companies"]) {
                    vue.setCompanies(vue.$store.getters["auth/companies"]);
                } else {
                    beat = setTimeout(checkCompaniesUntilDone, 500, this);
                }
            }

            let beat = setTimeout(checkCompaniesUntilDone, 500, this);
        },
        data() {
            return {
                company_current: null,
                companies_arr: [],
                companies_getter: this.$store.getters["auth/companies"]
            };
        },
        methods: {
            setCompanies(payload) {
                this.companies = [...(payload.owner), ...(payload.manager), ...(payload.employee)];
                this.company_current = this.companies.length > 0 ? this.companies[0] : null;
            }
        },
        computed: {
            companies: {
                get() {
                    return this.companies_arr;
                },
                set(companies) {
                    this.companies_arr = companies;
                }
            },
            positionTitle: {
                get() {
                    return this.company_current.rule_level ? this.company_current.rule_level.title : null
                }
            }
        },
    }
</script>

<style scoped>
    .get-face-nova {
        font-family: "Proxima Nova", sans-serif;
    }
</style>
