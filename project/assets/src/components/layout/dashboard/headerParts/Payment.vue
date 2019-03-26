<template>
    <span class="payment-holder">
        <display-days></display-days>
        <modal-button></modal-button>
    </span>
</template>

<script>
    import DisplayDays from './payment/DisplayDays'
    import ModalButton from './payment/ModalButton'

    export default {
        name: "get-face-header-payment",
        components: {
            'display-days': DisplayDays,
            'modal-button': ModalButton,
        }
    }
</script>

<style scoped>
    .payment-holder {
        display: inline-flex;
        flex-flow: row nowrap;
    }
</style>
