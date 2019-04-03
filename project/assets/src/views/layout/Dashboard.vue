<template>
    <div>
        <v-app>
            <kill-sidebar></kill-sidebar>

            <abn-header></abn-header>
            <v-content>
                <transition
                        name="zoom"
                        mode="out-in"
                >
                    <router-view></router-view>
                </transition>
            </v-content>

            <abn-footer></abn-footer>
        </v-app>

    </div>
</template>

<script>
    import Header from "./../../components/layout/dashboard/Header"
    import Footer from "./../../components/layout/dashboard/Footer"
    import Sidebar from "./../../components/layout/dashboard/Sidebar"

    export default {
        name: "abn-master",
        data: () => ({}),
        components: {
            "abn-header": Header,
            "abn-footer": Footer,
            'kill-sidebar': Sidebar
        },
        mounted() {
            this.$bus.$on("get-face-user-self-update", this.updateUserData);

            // make debounced check for token in system. If not, push user out.
            setTimeout(function (vue) {
                if (!vue.$store.getters['auth/token'] && !localStorage.getItem('token')) {
                    vue.$router.push({name: 'landing'})
                }

                let user = vue.$store.getters['auth/user'];

                if (!user || !user.id) {
                    vue.updateUserData();
                }
            }, 100, this);
        },
        methods: {
            updateUserData() {
                this.$http('auth.user')
                    .then(res => {
                        this.$bus.$emit("get-face-updated-companies", res.data.companies);
                        this.$store.commit('auth/setUser', res.data);

                        if (!this.$route.name.includes('dashboard')) this.$router.push({name: 'dashboard.main'});
                    })
                    .catch(err => {
                        let code = -1;
                        console.log(err);

                        if (err.response && (code = err.response.status)) {
                            (code == 401 || code == 403) && this.$store.dispatch('auth/logout').catch(e => {
                                /* just do nothing */
                            });
                        }
                    })
            },
        },
    }
</script>

<!-- Dashboard global styles -->
<style lang="css">
    .input-no-arrows input[type='number'] {
        -moz-appearance: textfield !important;
    }

    .input-no-arrows input::-webkit-outer-spin-button,
    .input-no-arrows input::-webkit-inner-spin-button {
        -webkit-appearance: none !important;
    }

    .zoom-enter-active,
    .zoom-leave-active {
        animation-duration: 0.1s;
        animation-fill-mode: both;
        animation-name: zoom;
    }

    .zoom-leave-active {
        animation-direction: reverse;
    }

    @keyframes zoom {
        from {
            opacity: 0;
        }

        100% {
            opacity: 1;
        }
    }
</style>
