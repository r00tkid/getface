<template>
    <v-select
            v-if="companies && companies.length > 0"
            :disabled="companies.length === 1"
            v-model="currentCompany"
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
        name: "get-face-header-companies",
        beforeMount() {
            /* Before */
        },
        data() {
            return {
                company_current: undefined,
            };
        },
        methods: {},
        computed: {
            companies: {
                get() {
                    return this.$store.getters['auth/companies'];
                },
            },
            company: {
                get() {
                    const that = this;

                    try {
                        return this.companies[this.companies.findIndex(function (company) {
                            return that.company_current == company.id;
                        })];
                    } catch (e) {
                        return undefined;
                    }
                }
            },
            currentCompany: {
                get() {
                    return this.company_current;
                },
                set(id) {
                    this.company_current = id;

                    let company = null;

                    if (id && (company = this.company)) {
                        this.$bus.$emit("get-face-company-changed", company);
                    }
                },
            },
        },
        watch: {
            companies(data) {
                if (data && data.length > 0 && !this.company_current) {
                    this.currentCompany = data[0].id;
                }
            },
        }
    }
</script>

<style scoped>
    .get-face-nova {
        font-family: "Proxima Nova", sans-serif;
    }
</style>
