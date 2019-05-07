<template>
  <div class="tableContainer">
    <table class="homeTable">
      <thead>
        <tr>
          <th v-for="(head,i) in headers" :key="i">
            <div v-for="(item,i) in head" :key="i">{{item}}</div>
          </th>
        </tr>
      </thead>
      <tbody v-for="(section, i) in tableData" :key="i">
        <tr>
          <td
            @click="hideGroup"
            class="tableSeparator white--text"
            colspan="999"
            style="text-align: left;"
          ></td>
        </tr>
        <tr v-for="(row,k) in section.items" :key="k">
          <td v-for="(item,l) in row" :key="l" :class="{come: item.come == true }">
            <template v-if="item.arrived.length != ''">
              <drag class="drag" :transfer-data="{ item }">
                <div>{{item.arrived}}</div>
                <div>{{item.left}}</div>
              </drag>
            </template>
            <template v-else>
              <drop class="drop" @drop="handleDrop" @dragover="dragEnd(i,k,l)">
                <div class="addTime" @click="addTime($event,i,k,l)"><v-icon medium color="purple">add_circle</v-icon></div>
              </drop>
            </template>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { log } from 'util';
export default {
  data() {
    return {
      headers: [],
      indexes: [],
      tableData: [
        {
          name: "Горячий цех",
          id: 0,
          items: [
            [
              { arrived: "09:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false },
              { arrived: "09:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false },
              { arrived: "09:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false },
              { arrived: "09:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false }
            ],
            [
              { arrived: "", left: "", come: false },
              { arrived: "09:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false },
              { arrived: "18:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false },
              { arrived: "09:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false },
              { arrived: "18:00", left: "18:00", come: true }
            ]
          ]
        },
        {
          name: "Холодный цех",
          id: 1,
          items: [
            [
              { arrived: "09:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false },
              { arrived: "09:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false },
              { arrived: "09:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false },
              { arrived: "09:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false }
            ],
            [
              { arrived: "", left: "", come: false },
              { arrived: "09:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false },
              { arrived: "18:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false },
              { arrived: "09:00", left: "18:00", come: true },
              { arrived: "", left: "", come: false },
              { arrived: "18:00", left: "18:00", come: true }
            ]
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
    },
    getDays() {
      let month = new Date().getMonth();
      let year = new Date().getFullYear();
      let date = new Date(year, month, 1);
      while (date.getMonth() === month) {
        let day = new Date(date).toLocaleDateString("en-GB", {
          weekday: "short",
          day: "2-digit"
        });
        this.headers.push(day.split(" "));
        date.setDate(date.getDate() + 1);
      }
    },
    handleDrop(data, event, ) {
      this.$set(this.tableData[this.indexes[0]].items[this.indexes[1]], this.indexes[2], data.item);
    },
    dragEnd(...rest){
      this.indexes = [...rest]
    },
    addTime(e,i,k,l){
      console.log(e.target.getBoundingClientRect());
    }
  },
  created() {
    this.getDays();
  }
};
</script>

<style scoped>
.drop,.drag{
  width: 45px;
  height: 42px;
}
.nameCell a {
  color: #fff !important;
}

.tableContainer {
  overflow: auto;
  max-height: 500px;
}

.nameCell {
  min-width: 250px;
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
  height: 26px;
  border: none;
  color: #fff;
  padding-left: 40px;
  cursor: pointer;
  background: #7d6df2;
  border-color: #7d6df2;
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
  background: linear-gradient(to top, #3dcb73, #84fcb5);
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
.addTime{
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  opacity: 0;
  transition: all 0.3s;
}
.addTime:hover{
  opacity: 1;
}
</style>

{
  
}
