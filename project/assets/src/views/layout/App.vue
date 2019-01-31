<template>
    <router-view></router-view>
</template>

<script>
    export default {
        name: "abn-master",
    }
</script>

<style>
    .primary {
        background: linear-gradient(to right top, #7d6df2, #9077f4, #a181f6, #b08bf9, #be96fb) !important;
    }

    .purple {
        color: #7d6df2 !important;
    }

    .purple--text, a {
        color: #7d6df2 !important;
    }

    .get-orange {
        background: linear-gradient(to right top, #f99342, #faa548, #fbb651, #fac75d, #fad86c) !important;
    }

    .orange, .orange--text {
        color: #f99342 !important;
    }

    .get-danger {
        background: linear-gradient(to right top, #ff6287, #ff687c, #ff6e72, #ff7569, #ff7d60) !important;
    }

    .get-danger--text {
        color: #ff687c !important;
    }

    .v-btn {
        text-transform: none;
        line-height: 15px;
    }
</style>
