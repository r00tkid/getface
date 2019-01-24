<template>
  <div class="tableContainer">
    <table class="homeTable">
      <thead>
        <tr class="tableHead">
          <th>
            <input type="checkbox">
          </th>
          <th>Ф.И.О</th>
          <th>Должность</th>
          <th>Кол-во
            <br>нарушений
          </th>
          <th>Недоработанные
            <br>часы
          </th>
          <th>Награды</th>
          <th>Настроение</th>
          <th>План рабочих
            <br>часов
          </th>
          <th>Факт отработанных
            <br>часов
          </th>
          <th>Кол-во
            <br>смен
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td @click="hideGroup" class="tableSeparator" colspan="999" style="text-align: left;">
            <span class="separatorText">Горячий цех</span>
          </td>
        </tr>
        <tr>
          <td>
            <input type="checkbox">
          </td>
          <td>
            <v-avatar size="30px" color="indigo">
              <v-icon dark>account_circle</v-icon>
            </v-avatar>
            <span class="staffName">Баренцев Владимир</span>
          </td>
          <td>Ст. Официант</td>
          <td>2</td>
          <td>1ч:45м</td>
          <td class="reward">&#9812;</td>
          <td>
            85%
            <span class="mood">&#9787;</span>
          </td>
          <td>180ч:30м</td>
          <td>180ч:30м</td>
          <td>19</td>
        </tr>
        <tr>
          <td>
            <input type="checkbox">
          </td>
          <td>
            <v-avatar size="30px" color="indigo">
              <v-icon dark>account_circle</v-icon>
            </v-avatar>
            <span class="staffName">Баренцев Владимир</span>
          </td>
          <td>Ст. Официант</td>
          <td>2</td>
          <td>1ч:45м</td>
          <td class="reward">&#9812;</td>
          <td>
            85%
            <span class="mood">&#9787;</span>
          </td>
          <td>180ч:30м</td>
          <td>180ч:30м</td>
          <td>19</td>
        </tr>
        <tr>
          <td>
            <input type="checkbox">
          </td>
          <td>
            <v-avatar size="30px" color="indigo">
              <v-icon dark>account_circle</v-icon>
            </v-avatar>
            <span class="staffName">Баренцев Владимир</span>
          </td>
          <td>Ст. Официант</td>
          <td>2</td>
          <td>1ч:45м</td>
          <td class="reward">&#9812;</td>
          <td>
            85%
            <span class="mood">&#9787;</span>
          </td>
          <td>180ч:30м</td>
          <td>180ч:30м</td>
          <td>19</td>
        </tr>
        <tr>
          <td>
            <input type="checkbox">
          </td>
          <td>
            <v-avatar size="30px" color="indigo">
              <v-icon dark>account_circle</v-icon>
            </v-avatar>
            <span class="staffName">Баренцев Владимир</span>
          </td>
          <td>Ст. Официант</td>
          <td>2</td>
          <td>1ч:45м</td>
          <td class="reward">&#9812;</td>
          <td>
            85%
            <span class="mood">&#9787;</span>
          </td>
          <td>180ч:30м</td>
          <td>180ч:30м</td>
          <td>19</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
  methods: {
    hideGroup(e) {
      if (e.target.className == "tableSeparator") {
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
  background-color: #a841ba;
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
.staffName{
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


