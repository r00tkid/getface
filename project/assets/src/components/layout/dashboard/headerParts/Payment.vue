<template>
    <span class="payment-holder">
        <v-btn large outline color="grey" disabled>{{ getTimeLeft }} Дней</v-btn>
        <v-btn large class="primary white--text">Оплатить</v-btn>
    </span>
</template>

<script>
    export default {
        name: "get-face-header-payment",
        mounted() {
            this.$bus.$on('get-face-company-changed', this.setTimeLeft);
        },
        data() {
            return {
                time_left: -1,
            };
        },
        methods: {
            setTimeLeft(company) {
                this.getTimeLeft = company.time_left;
            },
        },
        computed: {
            getTimeLeft: {
                get() {
                    return this.time_left;
                },
                set(value) {
                    console.log(value);

                    if (value < 0) {
                        this.time_left = value;
                        return;
                    }

                    function dhm(t) {
                        let cd = 24 * 60 * 60,
                            ch = 60 * 60,
                            d = Math.floor(t / cd),
                            h = Math.floor((t - d * cd) / ch),
                            m = Math.round((t - d * cd - h * ch) / 60000),
                            pad = function (n) {
                                return n < 10 ? '0' + n : n;
                            };

                        if (m === 60) {
                            h++;
                            m = 0;
                        }

                        if (h === 24) {
                            d++;
                            h = 0;
                        }

                        // TODO: get in the robot, Shinji
                        return `${d} дней ${pad(h)}:${pad(m)}`;
                    }

                    this.time_left = dhm(value);
                    console.log(this.time_left);
                },
            }
        },
    }
</script>

<style scoped>
    .payment-holder {
        display: inline-flex;
        flex-flow: row nowrap;
    }
</style>
