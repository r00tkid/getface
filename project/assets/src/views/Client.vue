<template>
  <v-container class="clientContainer" fluid>
    <v-layout align-start>
      <v-flex xs3 class="mr-2">
        <v-layout column>
          <v-flex class="materialBox">
            <h3 class="mb-2">Профиль</h3>
            <v-divider class="mb-2"></v-divider>
            <small>E-mail</small>
            <v-text-field readonly class="mb-2" hide-details v-model="profile.email" solo></v-text-field>
            <small>Название компании</small>
            <v-text-field
              hide-details
              class="editable-input mb-2"
              v-model="profile.company.value"
              solo
              type="text"
              :readonly="profile.company.readonly"
            >
              <template slot="append">
                <v-btn
                  @click="changeData($event)"
                  data-btn="company"
                  class="input-btn"
                  fab
                  dark
                  small
                  color="primary"
                >
                  <v-icon v-if="profile.company.readonly" dark>
                    edit
                  </v-icon>
                  <v-icon v-else dark>
                    save
                  </v-icon>
                  
                </v-btn>
              </template>
            </v-text-field>
            <small>Контактный телефон</small>
            <v-text-field
              hide-details
              class="editable-input mb-3"
              v-model="profile.phone.value"
              mask="+# ### ### ####"
              solo
              type="text"
              :readonly="profile.phone.readonly"
            >
              <template slot="append">
                <v-btn
                  @click="changeData($event)"
                  data-btn="phone"
                  class="input-btn"
                  fab
                  dark
                  small
                  color="primary"
                >
                  <v-icon v-if="profile.phone.readonly" dark>
                    edit
                  </v-icon>
                  <v-icon v-else dark>
                    save
                  </v-icon>
                </v-btn>
              </template>
            </v-text-field>
          </v-flex>
          <v-flex class="materialBox mt-2">
            <h3 class="mb-2">Смена пароля</h3>
            <v-divider class="mb-2"></v-divider>
            <small>Текущий пароль</small>
            <v-text-field class="mb-2" hide-details v-model="changePass.oldPass" solo></v-text-field>
            <small>Новый пароль</small>
            <v-text-field class="mb-2" hide-details v-model="changePass.newPass" solo></v-text-field>
            <small>Повторите новый пароль</small>
            <v-text-field class="mb-2" hide-details v-model="changePass.repeatNewPass" solo></v-text-field>
            <v-btn class="fullWidthBtn mt-3" large color="primary">Сохранить новый пароль</v-btn>
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex xs6 class="materialBox mr-2">sfgdfg</v-flex>
      <v-flex xs3>
        <v-layout column>
          <v-flex class="materialBox">
            <h3 class="mb-2">Часовой пояс</h3>
            <v-divider class="mb-2"></v-divider>
            <small>Ваша страна</small>
            <v-select :items="country" solo hide-details></v-select>
            <small>Ваш город</small>
            <v-select :items="city" solo hide-details></v-select>
            <div class="mt-2 timeButtons">
              <v-btn color="primary">Сохранить</v-btn>
              <v-btn outline color="gray">Отменить</v-btn>
            </div>
            <div class="forLawyers mt-3">
              <h4 class="mb-3">Для юридических лиц</h4>
              <p>
                Lorem Ipsum - это текст-"рыба",
                часто используемый в печати и вэб-дизайне.
                Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века.
                В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов,
                используя Lorem Ipsum для распечатки образцов.
              </p>
              <v-btn class="fullWidthBtn mt-3" large color="primary">Заключить договор</v-btn>
            </div>
          </v-flex>
          <v-flex>
            <v-btn class="fullWidthBtn mt-3 deleteProfile" large color="primary">
              Удалить профиль и все
              <br>связанные с ним данные
            </v-btn>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  name: "Client",
  data() {
    return {
      profile: {
        email: "test@test.com",
        phone: {
          value: "70505552234",
          readonly: true
        },
        company: {
          value: "AntHouse",
          readonly: true
        }
      },
      changePass: {
        oldPass: "",
        newPass: "",
        repeatNewPass: ""
      },
      country: ["Россия", "Беларусь", "Литва"],
      city: ["Москва", "Минск", "Рига"]
    };
  },
  methods: {
    changeData(e) {
      let id = e.target.parentNode.parentNode.getAttribute("data-btn");
      console.log(this.profile[id]);
      this.profile[id].readonly = !this.profile[id].readonly;
      
    }
  }
};
</script>
<style scoped>
.clientContainer {
  width: 90%;
}
.input-btn {
  height: 20px;
  width: 20px;
  position: relative;
  left: 10px;
}
.input-btn i {
  font-size: 13px !important;
}
.editable-input {
  position: relative;
}
.editable-input:after {
  content: "";
  position: absolute;
  display: inline-block;
  width: 1px;
  height: 40px;
  right: 40px;
  background-color: #ccc;
}
.fullWidthBtn {
  width: 100%;
  margin: 0;
}
.timeButtons {
  display: flex;
  justify-content: space-between;
}
.timeButtons button {
  width: 45%;
}
.forLawyers {
  text-align: center;
}
.forLawyers p {
  background-color: #f6f6f6;
  color: #7d6df2;
  text-align: left;
  padding: 5px;
}
.deleteProfile {
  height: 50px;
}
</style>

