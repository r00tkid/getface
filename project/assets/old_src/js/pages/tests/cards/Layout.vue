<template>
    <div>
        <v-tabs
                fixed-tabs
                slider-color="cyan darken-1"
                active-class="active"
        >
            <v-tab :to="{name:'test.cards.add'}">
                Добавление
            </v-tab>
            <v-tab :to="{name:'test.cards.show'}">
                Показ
            </v-tab>
        </v-tabs>
        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        name: "layout",
        data() {
            return {
                active: null,
            }
        },
    }
</script>