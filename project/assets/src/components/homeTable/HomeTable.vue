<template>
  <div class="tableContainer">
    <table class="homeTable">
      <thead>
        <tr class="tableHead">
          <th>
            <input type="checkbox">
          </th>
          <th v-for="(head,i) in headers" :key="i" v-html="head"></th>
        </tr>
      </thead>
      <tbody v-for="(section,i) in tableData" :key="i">
        <tr>
          <td
            @click="hideGroup($event,section.id)"
            class="tableSeparator white--text"
            colspan="999"
            style="text-align: left;"
          >
            <span class="separatorText">{{section.name}}</span>
          </td>
        </tr>
        <tr v-for="(employee,i) in section.employees" :key="i">
          <td>
            <input type="checkbox">
          </td>
          <td class="nameCell" style="height: 47px;">
            <div>
              <span class="staffName">{{employee.name}}</span>
              <div>
                <span class="rewards">
                  <v-icon>star</v-icon>
                </span>
                <router-link :to="{name: 'dashboard.employee'}">
                  <span class="linkProfile">
                    <v-icon>account_circle</v-icon>
                  </span>
                </router-link>
              </div>
            </div>
          </td>
          <td class="mainCell">{{employee.position}}</td>
          <td class="mainCell">{{employee.violations}}</td>
          <td class="mainCell">{{employee.shifts}}</td>
          <td class="mainCell">{{employee.timeFact}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      headers: ['Ф.И.О', 'Должность','Кол-во<br> нарушений','Кол-во<br> смен', 'Разность<br> План/Факт'],
      tableData: [
        {
          name: "Гарячий цех",
          id: 0,
          opened: true,
          employees: [
            {
              name: "Баренцев Владимир",
              position: "Ст.Официант",
              violations: "2",
              timeFact: "180ч:30м",
              shifts: "19"
            },
            {
              name: "Василий Орехов",
              position: "Ст.Официант",
              violations: "2",
              timeFact: "180ч:30м",
              shifts: "19"
            }
          ]
        },
        {
          name: "Холодный цех",
          id: 1,
          opened: true,
          employees: [
            {
              name: "Адриано Челентано",
              position: "Ст.Официант",
              violations: "2",
              timeFact: "180ч:30м",
              shifts: "19"
            },
            {
              name: "Тони Старк",
              position: "Ст.Официант",
              violations: "2",
              timeFact: "180ч:30м",
              shifts: "19"
            }
          ]
        },
      ]
    };
  },
  methods: {
    hideGroup(e, id) {
      console.log(id);
      
      if (e.target.className.includes("tableSeparator")) {
        let tableBody = e.target.parentElement.parentElement;
        let bodyElements = tableBody.childNodes;

        bodyElements.forEach((element, i) => {
          if (i > 0 && element.style.display == "none") {
            element.style.display = "table-row";
          } else if (i > 0) {
            element.style.display = "none";
          }
        });
      }
    }
  }
};
</script>

<style scoped>
.nameCell a {
  color: #fff !important;
}

.tableContainer {
  overflow: auto;
  max-height: 500px;
}

.nameCell {
  min-width: 200px;
}

.nameCell div {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.linkProfile {
  padding: 5px;
  border-left: 1px solid #d4d4d4;
  cursor: pointer;
}

.rewards i {
  font-size: 16px;
  color: #fbbd21;
  margin-right: 2px;
}

.mainCell {
  min-width: 50px;
}

th,
td {
  border: 1px solid #d4d4d4;
  border-collapse: collapse;
  background-color: #fff;
  padding: 2px 5px;
}

table {
  width: 100%;
  border-collapse: collapse;
  box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
    0 1px 5px 0 rgba(0, 0, 0, 0.12);
}

.tableSeparator {
  color: #fff;
  padding-left: 40px;
  cursor: pointer;
  background: #7d6df2;
  border-color: #7d6df2;
  border: none;
  border-right: 1px solid #7d6df2;
}

.separatorText {
  position: relative;
}

.separatorText::after {
  content: "";
  position: absolute;
  top: 7px;
  right: -10px;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 5px 2.5px 0 2.5px;
  border-color: #ffffff transparent transparent transparent;
}

.come {
  background-color: #5adf8e;
}

.notCome {
  background-color: #fa6d74;
}

.calendarTD {
  padding: 0;
  color: #fff;
  min-width: 45px;
  min-height: 45px;
}

.calendarTD div {
  padding: 1px 3px;
}

.tableContainer::-webkit-scrollbar {
  width: 7px;
  height: 7px;
}

.tableContainer::-webkit-scrollbar-button {
  display: none;
}

.tableContainer::-webkit-scrollbar-track {
  background-color: #969696;
}

.tableContainer::-webkit-scrollbar-track-piece {
  background-color: #d4d4d4;
}

.tableContainer::-webkit-scrollbar-thumb {
  height: 50px;
  background-color: #969696;
  border-radius: 3px;
}

.tableContainer::-webkit-scrollbar-corner {
  display: none;
}

.tableContainer::-webkit-resizer {
  background-color: #969696;
}
</style>

{
  
}
