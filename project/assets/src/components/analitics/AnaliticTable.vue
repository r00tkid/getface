<template>
  <div>
    <ul class="tableHeaders">
      <li class="tableHeaders-item settings-item">
        <v-icon small>settings</v-icon>
      </li>
      <li class="tableHeaders-item" v-html="headers.name"></li>
      <li class="tableHeaders-item" v-html="headers.amount"></li>
      <li class="tableHeaders-item" v-html="headers.mood"></li>
      <li class="tableHeaders-item" v-html="headers.male"></li>
      <li class="tableHeaders-item average" v-html="headers.female"></li>
      <li class="tableHeaders-item average" v-html="headers.averageTime"></li>
      <li class="tableHeaders-item" v-html="headers.heavyCars"></li>
      <li class="tableHeaders-item" v-html="headers.lightCars"></li>
    </ul>
    <v-data-table
      hide-headers
      :headers-length="headersLength"
      :items="mainItems"
      item-key="name"
      hide-actions
    >
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
        <v-data-table
          hide-headers
          :headers-length="headersLength"
          :items="props.item.items"
          item-key="name2"
          hide-actions
        >
          <template slot="items" scope="props">
            <tr @click="props.expanded = !props.expanded">
              <td class="text-xs-right">
                <v-checkbox
                  class="tableCheckbox"
                  v-model="props.item.selected"
                  primary
                  hide-details
                ></v-checkbox>
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
        </v-data-table>
      </template>
    </v-data-table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      selected: [],
      headersLength: 9,
      headers: {
        name: "Название камеры",
        amount: "Количество посетителей",
        mood: "Настроение",
        male: "Мужчин",
        female: "Женщин",
        averageTime: "Среднее время присутствия",
        heavyCars: "Грузовых <br> автомобилей",
        lightCars: "Легковых <br> автомобилей"
      },
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
.tableCheckbox {
  position: relative;
  left: 20px;
}
.tableHeaders {
  display: flex;
  justify-content: space-around;
  list-style: none;
  background-color: #fff;
  border: 1px solid #d4d4d4;
  border-radius: 3px 3px 0 0;
  width: 100%;
  padding: 5px 0;
}
.tableHeaders-item {
  flex: 2;
  display: flex;
  text-align: center;
  justify-content: center;
  align-items: center;
}
.settings-item {
  flex: 1;
}
.average{
  position: relative;
  left: 24px;
}
</style>


