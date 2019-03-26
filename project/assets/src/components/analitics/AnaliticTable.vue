<template>
  <v-data-table :headers="mainHeaders" :items="mainItems" item-key="name" hide-actions>
    <template slot="headers" scope="props">
      <tr>
        <th><v-icon small>settings</v-icon></th>
        <th
          v-for="header in props.headers"
          :key="header.text"
        >
          {{ header.text }}
        </th>
      </tr>
    </template>
    <template slot="items" scope="props">
      <tr @click="props.expanded = !props.expanded">
        <td>
          <v-checkbox :input-value="props.item.selected" primary hide-details></v-checkbox>
        </td>
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
    <template slot="expand" slot-scope="props" v-if="props.item.items">
      <v-data-table hide-headers :headers-length="headersLength" :items="props.item.items" item-key="name2" hide-actions>
        <template slot="items" scope="props">
          <tr @click="props.expanded = !props.expanded">
            <td>
              <v-checkbox v-model="props.item.selected" primary hide-details></v-checkbox>
            </td>
            <td class="text-xs-right">{{ props.item.name }}</td>
            <td class="text-xs-right">{{ props.item.amount }}</td>
            <td class="text-xs-right">{{ props.item.mood }}</td>
            <td class="text-xs-right">{{ props.item.male }}</td>
            <td class="text-xs-right">{{ props.item.female }}</td>
            <td class="text-xs-right">{{ props.item.averageTime }}</td>
            <td class="text-xs-right">{{ props.item.heavyCars }}</td>
            <td class="text-xs-right">{{ props.item.lightCars }}</td>
            <td class="text-xs-right">{{ props.item.lightCars }}</td>
          </tr>
        </template>
      </v-data-table>
    </template>
  </v-data-table>
</template>
<script>
export default {
  data() {
    return {
      selected: [],
      headersLength: 10,
      mainHeaders: [
        { text: "Название камеры", value: "name" },
        { text: "Количество посетителей", value: "amount" },
        { text: "Настроение", value: "mood" },
        { text: "Мужчин", value: "male" },
        { text: "Женщин", value: "female" },
        { text: "Среднее время присутствия", value: "averageTime" },
        { text: "Грузовых автомобилей", value: "heavyCars" },
        { text: "Легковых автомобилей", value: "lightCars" },
        {}
      ],
      subHeaders: [
        { text: "Название камеры", value: "name" },
        { text: "Количество посетителей", value: "amount" },
        { text: "Настроение", value: "mood" },
        { text: "Мужчин", value: "male" },
        { text: "Женщин", value: "female" },
        { text: "Среднее время присутствия", value: "averageTime" },
        { text: "Грузовых автомобилей", value: "heavyCars" },
        { text: "Легковых автомобилей", value: "lightCars" }
      ],
      mainItems: [
        {
          name: "Камера 1",
          selected: true,
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
          selected: true,
          amount: "500 чел (15%)",
          mood: "Плохое-15%",
          male: "250 чел (50%)",
          female: "250 чел (50%)",
          averageTime: "150ч:30м",
          heavyCars: "250 (50%)",
          lightCars: "250 (50%)"
        },
        {
          name: "Зона 1",
          selected: true,
          amount: "500 чел (15%)",
          mood: "Плохое-15%",
          male: "250 чел (50%)",
          female: "250 чел (50%)",
          averageTime: "150ч:30м",
          heavyCars: "250 (50%)",
          lightCars: "250 (50%)",
          items: [
            {
              name: "Камера 5",
              selected: true,
              amount: "500 чел (15%)",
              mood: "Плохое-15%",
              male: "250 чел (50%)",
              female: "250 чел (50%)",
              averageTime: "150ч:30м",
              heavyCars: "250 (50%)",
              lightCars: "250 (50%)"
            },
            {
              name: "Камера 6",
              selected: true,
              amount: "500 чел (15%)",
              mood: "Плохое-15%",
              male: "250 чел (50%)",
              female: "250 чел (50%)",
              averageTime: "150ч:30м",
              heavyCars: "250 (50%)",
              lightCars: "250 (50%)"
            }
          ]
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


