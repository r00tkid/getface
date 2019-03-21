<template>
  <div id="chartHeatMap">
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
            max: 600
          })
        },
        {
          name: "Вт.",
          data: this.generateData(23, {
            min: 0,
            max: 600
          })
        },
        {
          name: "Ср.",
          data: this.generateData(23, {
            min: 0,
            max: 600
          })
        },
        {
          name: "Чт.",
          data: this.generateData(23, {
            min: 0,
            max: 600
          })
        },
        {
          name: "Пт.",
          data: this.generateData(23, {
            min: 0,
            max: 600
          })
        },
        {
          name: "Сб.",
          data: this.generateData(23, {
            min: 0,
            max: 600
          })
        },
        {
          name: "Вс.",
          data: this.generateData(23, {
            min: 0,
            max: 600
          })
        }
      ],
      chartOptions: {
        dataLabels: {
          enabled: false
        },
        legend:{
          position: 'bottom',
          offsetY: -13,
        },
        xaxis: {
          type: 'category',
          labels: {
            rotate: -45,
            style: {
              fontSize: '11px',
            },
            offsetX: 3
          },
          tickPlacement: 'between',
          axisTicks: {
            show: false
          },
          axisBorder:{
            show: false
          }
        },
        plotOptions: {
          heatmap: {
            radius: 5,
            enableShades: false,
            shadeIntensity: 0.9,
            colorScale: {
              ranges: [
                {
                  from: 0,
                  to: 100,
                  name: "До 100",
                  color: "#f4f4f4"
                },
                {
                  from: 101,
                  to: 200,
                  name: "100-200",
                  color: "#a3d5fd"
                },
                {
                  from: 201,
                  to: 300,
                  name: "200-300",
                  color: "#a3d5fd"
                },
                {
                  from: 301,
                  to: 400,
                  name: "300-400",
                  color: "#5fa9ea"
                },
                {
                  from: 401,
                  to: 500,
                  name: "400-500",
                  color: "#4292e1"
                },
                {
                  from: 501,
                  to: 600,
                  name: "500-600",
                  color: "#3180d9"
                }
              ]
            }
          }
        }
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
#chartHeatMap{
  margin-top: -32px;
}
</style>


