<template>
    <div>
        <v-app>
            <kill-sidebar></kill-sidebar>

            <abn-header></abn-header>
            <v-content>
                <transition name="zoom"
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
    import Header from "./../../components/layout/Header"
    import Footer from "./../../components/layout/Footer"
    import Sidebar from "./../../components/layout/Sidebar"


    export default {
        name: "abn-master",
        data: () => ({}),

        components: {
            "abn-header": Header,
            "abn-footer": Footer,
            'kill-sidebar': Sidebar
        }
    }
</script>

<!-- Global project styles -->
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
            transform: scale3d(0.3, 0.3, 0.3);
        }

        100% {
            opacity: 1;
        }
    }

</style>
