<template>
  <div id="chart">
    <apexchart type="heatmap" :options="chartOptions" :series="series"/>
  </div>
</template>
<script>
export default {
  data() {
    return {
      series: [
        {
          name: "Пн.",
          data: this.generateData(23, {
            min: 0,
            max: 90
          })
        },
        {
          name: "Вт.",
          data: this.generateData(23, {
            min: 0,
            max: 90
          })
        },
        {
          name: "Ср.",
          data: this.generateData(23, {
            min: 0,
            max: 90
          })
        },
        {
          name: "Чт.",
          data: this.generateData(23, {
            min: 0,
            max: 90
          })
        },
        {
          name: "Пт.",
          data: this.generateData(23, {
            min: 0,
            max: 90
          })
        },
        {
          name: "Сб.",
          data: this.generateData(23, {
            min: 0,
            max: 90
          })
        },
        {
          name: "Вс.",
          data: this.generateData(23, {
            min: 0,
            max: 90
          })
        }
      ],
      chartOptions: {
        dataLabels: {
          enabled: false
        },
        plotOptions: {
          heatmap: {
            radius: 5,
            enableShades: true,
            shadeIntensity: 0.5,
          }
        },
        colors: ["#008FFB"]
      }
    };
  },
  methods: {
    generateData(count, yrange) {
      let i = 0;
      let series = [];
      while (i < count) {
        let x = i.toString() + ":00";
        let y =
          Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
          yrange.min;

        series.push({
          x: x,
          y: y
        });
        i++;
      }
      return series;
    }
  }
};
</script>
<style>
.apexcharts-menu-icon {
  display: none;
}
</style>


