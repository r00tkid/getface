<template>
    <span>
        <v-btn large class="primary white--text" @click="modal_state = !modal_state">Оплатить</v-btn>
        <payment-modal :modal_state="modal_state" :parent="getThis"></payment-modal>
    </span>
</template>

<script>
    export default {
        name: "modal-button",
        data() {
            return {
                modal_state: false,
            }
        },
        components: {
            'payment-modal': () => import('./../../../../modals/payment/CompanyPay')
        },
        methods: {
            getThis() {
                return this;
            }
        }
    }
</script>
