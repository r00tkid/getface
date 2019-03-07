<template>
    <v-select
            v-model="currentLang"
            :items="items"
            class="kill-select"
            item-value="locale"
            item-text="visual"
            hide-selected
            solo
            flat
    ></v-select>
</template>

<script>
    export default {
        name: "get-face-header-locale",
        data() {
            return {
                currentLang: this.$locale,
                items: [
                    {
                        locale: this.$locale,
                        visual: "ru" === this.$locale ? "Рус" : "Eng",
                    },
                    {
                        locale: this.$fallbackLocale,
                        visual: "ru" === this.$fallbackLocale ? "Рус" : "Eng",
                    },
                ],
            };
        },
        watch: {
            currentLang(val) {
                this.$locale = val;
                this.$bus.$emit("gat-face-changed-locale", val);
            },
        },
    }
</script>
