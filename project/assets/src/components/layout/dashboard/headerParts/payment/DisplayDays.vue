<template>
    <v-btn large outline color="grey" disabled v-if="timeless" v-html="tick_play"></v-btn>
    <v-btn large outline color="grey" disabled v-else v-html="display_time_left"></v-btn>
</template>

<script>
    export default {
        name: "display-days",
        beforeMount() {
            this.$bus.$on('get-face-company-changed', this.setTimeLeft);
        },
        data() {
            return {
                time_left: `<span style="color: #ff0000">-0 деней</span>`,
                timer_counter: null,
                t_days: 0,
                t_hours: 0,
                t_minutes: 0,
                t_seconds: 0,
                company: null,
                changed_company: true,
            };
        },
        methods: {
            setTimeLeft(company) {
                this.changed_company = true;

                if (this.company && this.company.id && !this.t_days) {
                    this.company.time_left = this.t_hours * 60 * 60 + this.t_minutes * 60 + this.t_seconds;
                }

                this.c_hours
                    = this.c_minutes
                    = this.c_seconds
                    = this.t_days
                    = 0;

                if (this.timer_counter != null) {
                    clearTimeout(this.timer_counter);
                    this.timeless = null;
                }

                this.company = company;

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
                if (time_in_seconds <= 0 || isNaN(time_in_seconds)) return `<span style="color: #ff0000">-0 дней</span>`;

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

                if (days) {
                    this.t_days = days;

                    return `<span style="color: #002000">${days} дней</span>`;
                } else {
                    if (!this.timer_counter || this.changed_company) {
                        this.changed_company = false;

                        this.c_hours = hours;
                        this.c_minutes = minutes;
                        this.c_seconds = seconds;

                        function ticker(vue) {
                            vue.t_seconds = vue.t_seconds - 1;

                            if (vue.t_seconds < 0) {
                                vue.t_minutes = vue.t_minutes - 1;
                                vue.c_seconds = 59;
                            }

                            if (vue.t_minutes < 0) {
                                vue.t_hours = vue.t_hours - 1;
                                vue.c_minutes = 59;
                            }

                            if (vue.t_hours < 0) {
                                clearTimeout(this.timer_counter);
                                vue.timeless = null;
                                vue.time_left = `<span style="color: #ff0000">0 деней</span>`;
                                return;
                            }

                            // vue.$log("tick-tack", vue.c_hours, ":", vue.c_minutes, ":", vue.c_seconds);

                            vue.timeless = setTimeout(ticker, 1000, vue);
                        }

                        this.timeless = setTimeout(ticker, 1000, this);
                    }

                    return "timer:timer:timer";
                }
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
            },
            timeless: {
                get() {
                    return this.timer_counter;
                },
                set(timer) {
                    this.timer_counter = timer;
                }
            },
            c_hours: {
                get() {
                    return this.pad(this.t_hours);
                },
                set(hours) {
                    this.t_hours = hours;
                }
            },
            c_minutes: {
                get() {
                    return this.pad(this.t_minutes);
                },
                set(minutes) {
                    this.t_minutes = minutes;
                }
            },
            c_seconds: {
                get() {
                    return this.pad(this.t_seconds);
                },
                set(seconds) {
                    this.t_seconds = seconds;
                }
            },
            tick_play: {
                get() {
                    return `<span style="color: #ff0000">${this.c_hours}:${this.c_minutes}:${this.c_seconds}</span>`;
                }
            }
        },
    }
</script>
