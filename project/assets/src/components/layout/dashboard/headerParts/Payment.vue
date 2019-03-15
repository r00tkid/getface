<template>
    <span class="payment-holder">
        <v-btn large outline color="grey" disabled v-html="display_time_left"></v-btn>
        <v-btn large class="primary white--text">Оплатить</v-btn>
    </span>
</template>

<script>
    export default {
        name: "get-face-header-payment",
        beforeMount() {
            this.$bus.$on('get-face-company-changed', this.setTimeLeft);
        },
        data() {
            return {
                time_left: `<span style="color: #ff0000">-1 день</span>`,
            };
        },
        methods: {
            setTimeLeft(company) {
                if (!company) {
                    company = {time_left: 0};
                }

                this.display_time_left = this.dayHoursMinutes(company.time_left);
            },
            pad(n) {
                return n < 10 ? '0' + n : n;
            },
            dayHoursMinutes(time_in_seconds) {
                time_in_seconds = parseFloat(time_in_seconds);
                if (time_in_seconds < 0 || isNaN(time_in_seconds)) return `<span style="color: #ff0000">-1 день</span>`;
                if (time_in_seconds === 0) return `<span style="color: #9acd32">Not allowed</span>`;

                // Time in seconds, not milliseconds or microseconds
                let seconds_day = 24 * 60 * 60,
                    seconds_hour = 60 * 60,
                    seconds_minute = 60,
                    days = Math.floor(time_in_seconds / seconds_day),
                    hours = Math.floor((time_in_seconds - days * seconds_day) / seconds_hour),
                    minutes = Math.floor((time_in_seconds - days * seconds_day - hours * seconds_hour) / seconds_minute),
                    seconds = Math.round(time_in_seconds - days * seconds_day - hours * seconds_hour - minutes * seconds_minute);

                if (seconds === 60) {
                    minutes++;
                    seconds = 0;
                }

                if (minutes === 60) {
                    hours++;
                    minutes = 0;
                }

                if (hours === 24) {
                    days++;
                    hours = 0;
                }

                if (days) return `<span style="color: #002000">${days} дней</span>`;
                else return `<span style="color: #ff0000">${this.pad(hours)}:${this.pad(minutes)}:${this.pad(seconds)}</span>`
            }
        },
        computed: {
            display_time_left: {
                get() {
                    return this.time_left;
                },
                set(value) {
                    this.time_left = value;
                }
            }
        }
    }
</script>

<style scoped>
    .payment-holder {
        display: inline-flex;
        flex-flow: row nowrap;
    }
</style>
