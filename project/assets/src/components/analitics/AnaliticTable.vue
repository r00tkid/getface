<template>
  <v-data-table
    :headers="mainHeaders"
    :items="mainItems"
    item-key="name"
    hide-actions
    expand
    class="elevation-1"
  >
    <template slot="items" scope="props">
      <tr @click="props.expanded = !props.expanded">
        <td class="text-xs">{{ props.item.name }}</td>
        <td class="text-xs">{{ props.item.amount }}</td>
        <td class="text-xs">{{ props.item.mood }}</td>
        <td class="text-xs">{{ props.item.male }}</td>
        <td class="text-xs">{{ props.item.female }}</td>
        <td class="text-xs">{{ props.item.averageTime }}</td>
        <td class="text-xs">{{ props.item.heavyCars }}</td>
        <td class="text-xs">{{ props.item.lightCars }}</td>
      </tr>
    </template>
  </v-data-table>
</template>
<script>
export default {
  data() {
    return {
      selected: [],
      mainHeaders: [
        { text: "Название камеры", value: "name" },
        { text: "Количество посетителей", value: "amount" },
        { text: "Настроение", value: "mood" },
        { text: "Мужчин", value: "male" },
        { text: "Женщин", value: "female" },
        { text: "Среднее время присутствия", value: "averageTime" },
        { text: "Грузовых автомобилей", value: "heavyCars" },
        { text: "Легковых автомобилей", value: "lightCars" }
      ],
      subHeaders: [],
      mainItems: [
        {
          name: "Камера 1",
          amount: "500 чел (15%)",
          mood: "Плохое-15%",
          male: "250 чел (50%)",
          female: "250 чел (50%)",
          averageTime: "150ч:30м",
          heavyCars: "250 (50%)",
          lightCars: "250 (50%)"
        },
        {
          name: "Камера 2",
          amount: "500 чел (15%)",
          mood: "Плохое-15%",
          male: "250 чел (50%)",
          female: "250 чел (50%)",
          averageTime: "150ч:30м",
          heavyCars: "250 (50%)",
          lightCars: "250 (50%)"
        },
        {
          name: "Камера 3",
          amount: "500 чел (15%)",
          mood: "Плохое-15%",
          male: "250 чел (50%)",
          female: "250 чел (50%)",
          averageTime: "150ч:30м",
          heavyCars: "250 (50%)",
          lightCars: "250 (50%)"
        }
      ],
       subItems: [
        {
          name: "Камера 1",
          amount: "500 чел (15%)",
          mood: "Плохое-15%",
          male: "250 чел (50%)",
          female: "250 чел (50%)",
          averageTime: "150ч:30м",
          heavyCars: "250 (50%)",
          lightCars: "250 (50%)"
        },
        {
          name: "Камера 2",
          amount: "500 чел (15%)",
          mood: "Плохое-15%",
          male: "250 чел (50%)",
          female: "250 чел (50%)",
          averageTime: "150ч:30м",
          heavyCars: "250 (50%)",
          lightCars: "250 (50%)"
        },
        {
          name: "Камера 3",
          amount: "500 чел (15%)",
          mood: "Плохое-15%",
          male: "250 чел (50%)",
          female: "250 чел (50%)",
          averageTime: "150ч:30м",
          heavyCars: "250 (50%)",
          lightCars: "250 (50%)"
        }
      ]
    };
  },
  methods: {
    toggleAll() {
      if (this.selected.length) this.selected = [];
      else this.selected = this.desserts.slice();
    },
    changeSort(column) {
      if (this.pagination.sortBy === column) {
        this.pagination.descending = !this.pagination.descending;
      } else {
        this.pagination.sortBy = column;
        this.pagination.descending = false;
      }
    }
  }
};
</script>
<style scoped>
</style>


