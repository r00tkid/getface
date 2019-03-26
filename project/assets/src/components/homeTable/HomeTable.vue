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
          <th>Кол-во нарушений</th>
          <th>Кол-во смен</th>
          <th>Разность План/Факт</th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
          <th>
            <div>01</div>
            <div>Пн</div>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td
            @click="hideGroup"
            class="tableSeparator primary white--text"
            colspan="999"
            style="text-align: left;"
          >
            <span class="separatorText">Горячий цех</span>
          </td>
        </tr>
        <tr>
          <td>
            <input type="checkbox">
          </td>
          <td class="nameCell">
            <div>
              <span class="staffName">Баренцев Владимир</span>
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
          <td class="mainCell">Ст. Официант</td>
          <td class="mainCell">2</td>
          <td class="mainCell">2/16</td>
          <td class="mainCell">+20ч : 30 м</td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime notCome">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime"></div>
            <div class="goneTime"></div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
        </tr>
        <tr>
          <td>
            <input type="checkbox" aria-label="Select">
          </td>
          <td class="nameCell">
            <div>
              <span class="staffName">Баренцев Владимир</span>
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
          <td class="mainCell">Ст. Официант</td>
          <td class="mainCell">2</td>
          <td class="mainCell">2/16</td>
          <td class="mainCell">+20ч : 30 м</td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime notCome">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime"></div>
            <div class="goneTime"></div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
        </tr>
        <tr>
          <td>
            <input type="checkbox">
          </td>
          <td class="nameCell">
            <div>
              <span class="staffName">Баренцев Владимир</span>
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
          <td class="mainCell">Ст. Официант</td>
          <td class="mainCell">2</td>
          <td class="mainCell">2/16</td>
          <td class="mainCell">+20ч : 30 м</td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime notCome">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime"></div>
            <div class="goneTime"></div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
        </tr>
      </tbody>
      <tbody>
        <tr>
          <td
            @click="hideGroup"
            class="tableSeparator primary white--text"
            colspan="999"
            style="text-align: left;"
          >
            <span class="separatorText">Горячий цех</span>
          </td>
        </tr>
        <tr>
          <td>
            <input type="checkbox">
          </td>
          <td class="nameCell">
            <div>
              <span class="staffName">Баренцев Владимир</span>
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
          <td class="mainCell">Ст. Официант</td>
          <td class="mainCell">2</td>
          <td class="mainCell">2/16</td>
          <td class="mainCell">+20ч : 30 м</td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime notCome">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime"></div>
            <div class="goneTime"></div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
        </tr>
        <tr>
          <td>
            <input type="checkbox" aria-label="Select">
          </td>
          <td class="nameCell">
            <div>
              <span class="staffName">Баренцев Владимир</span>
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
          <td class="mainCell">Ст. Официант</td>
          <td class="mainCell">2</td>
          <td class="mainCell">2/16</td>
          <td class="mainCell">+20ч : 30 м</td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime notCome">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime"></div>
            <div class="goneTime"></div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
        </tr>
        <tr>
          <td>
            <input type="checkbox">
          </td>
          <td class="nameCell">
            <div>
              <span class="staffName">Баренцев Владимир</span>
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
          <td class="mainCell">Ст. Официант</td>
          <td class="mainCell">2</td>
          <td class="mainCell">2/16</td>
          <td class="mainCell">+20ч : 30 м</td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime notCome">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime"></div>
            <div class="goneTime"></div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
        </tr>
      </tbody>
      <tbody>
        <tr>
          <td
            @click="hideGroup"
            class="tableSeparator primary white--text"
            colspan="999"
            style="text-align: left;"
          >
            <span class="separatorText">Горячий цех</span>
          </td>
        </tr>
        <tr>
          <td>
            <input type="checkbox">
          </td>
          <td class="nameCell">
            <div>
              <span class="staffName">Баренцев Владимир</span>
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
          <td class="mainCell">Ст. Официант</td>
          <td class="mainCell">2</td>
          <td class="mainCell">2/16</td>
          <td class="mainCell">+20ч : 30 м</td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime notCome">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime"></div>
            <div class="goneTime"></div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
        </tr>
        <tr>
          <td>
            <input type="checkbox">
          </td>
          <td class="nameCell">
            <div>
              <span class="staffName">Баренцев Владимир</span>
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
          <td class="mainCell">Ст. Официант</td>
          <td class="mainCell">2</td>
          <td class="mainCell">2/16</td>
          <td class="mainCell">+20ч : 30 м</td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime notCome">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime"></div>
            <div class="goneTime"></div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
        </tr>
        <tr>
          <td>
            <input type="checkbox">
          </td>
          <td class="nameCell">
            <div>
              <span class="staffName">Баренцев Владимир</span>
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
          <td class="mainCell">Ст. Официант</td>
          <td class="mainCell">2</td>
          <td class="mainCell">2/16</td>
          <td class="mainCell">+20ч : 30 м</td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime notCome">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime"></div>
            <div class="goneTime"></div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
          <td class="calendarTD">
            <div class="comingTime come">9:00</div>
            <div class="goneTime come">18:00</div>
          </td>
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
  border-color: #969696 !important;
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
