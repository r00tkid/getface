<template>
  <apexchart height="400" type="line" :options="lineOptions" :series="chartdata"></apexchart>
</template>
<script>
export default {
  props: {
    chartdata: {
      type: Array,
      default: null
    },
    lineOptions: {
      type: Object,
      default: null
    }
  },
};
</script>
<style scoped>
</style>


