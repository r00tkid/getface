<template>
  <div class="tableContainer">
    <table class="homeTable">
      <thead>
        <tr class="tableHead">
          <th>
            <input type="checkbox">
          </th>
          <th v-for="(head,i) in headers" :key="i">{{head}}</th>
        </tr>
      </thead>
      <tbody v-for="(section,i) in tableData" :key="i">
        <tr>
          <td
            @click="hideGroup"
            class="tableSeparator white--text"
            colspan="999"
            style="text-align: left;"
          >
            <span class="separatorText">{{section.name}}</span>
          </td>
        </tr>
        <tr v-for="(employee, i) in section.employees" :key="i">
          <td>
            <input type="checkbox">
          </td>
          <td>
            <v-avatar size="30px" color="indigo">
              <v-icon dark>account_circle</v-icon>
            </v-avatar>
            <span class="staffName">{{employee.name}}</span>
          </td>
          <td>{{employee.position}}</td>
          <td>{{employee.violations}}</td>
          <td>{{employee.unfinished}}</td>
          <td class="reward">{{employee.revards}}</td>
          <td>{{employee.mood}}</td>
          <td>{{employee.timePlan}}</td>
          <td>{{employee.timeFact}}</td>
          <td>{{employee.shifts}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      headers: [
        "Ф.И.О",
        "Должность",
        "Кол-во нарушений",
        "Недоработанные часы",
        "Награды",
        "Настроение",
        "План рабочих часов",
        "Факт отработанных часов",
        "Кол-во смен"
      ],
      tableData: [
        {
          name: "Гарячий цех",
          employees: [
            {
              name: "Баренцев Владимир",
              position: "Ст.Официант",
              violations: "2",
              unfinished: "1ч:45м",
              revards: "♔",
              mood: "85% ☻",
              timePlan: "180ч:30м",
              timeFact: "180ч:30м",
              shifts: "19"
            },
            {
              name: "Баренцев Владимир",
              position: "Ст.Официант",
              violations: "2",
              unfinished: "1ч:45м",
              revards: "♔",
              mood: "85% ☻",
              timePlan: "180ч:30м",
              timeFact: "180ч:30м",
              shifts: "19"
            }
          ]
        },
        {
          name: "Гарячий цех",
          employees: [
            {
              name: "Баренцев Владимир",
              position: "Ст.Официант",
              violations: "2",
              unfinished: "1ч:45м",
              revards: "♔",
              mood: "85% ☻",
              timePlan: "180ч:30м",
              timeFact: "180ч:30м",
              shifts: "19"
            },
            {
              name: "Баренцев Владимир",
              position: "Ст.Официант",
              violations: "2",
              unfinished: "1ч:45м",
              revards: "♔",
              mood: "85% ☻",
              timePlan: "180ч:30м",
              timeFact: "180ч:30м",
              shifts: "19"
            }
          ]
        }
      ]
    };
  },
  methods: {
    hideGroup(e) {
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
.tableContainer {
  overflow: auto;
  max-height: 500px;
}

.nameCell {
  min-width: 250px;
}

.mainCell {
  min-width: 150px;
}

th,
td {
  border: 1px solid #d4d4d4;
  border-collapse: collapse;
  background-color: #fff;
  padding: 2px 5px;
}

table {
  border-collapse: collapse;
  min-width: 1270px;
  box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
    0 1px 5px 0 rgba(0, 0, 0, 0.12);
}

.tableSeparator {
  background: linear-gradient(
    to right top,
    #7d6df2,
    #9077f4,
    #a181f6,
    #b08bf9,
    #be96fb
  ) !important;
  color: #fff;
  padding-left: 40px;
  cursor: pointer;
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

.reward {
  font-size: 25px;
  color: #f6a944;
}

.mood {
  font-size: 25px;
  color: #5ae08f;
}

.staffName {
  margin-left: 10px;
}

.tableContainer::-webkit-scrollbar {
  width: 5px;
  height: 5px;
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


