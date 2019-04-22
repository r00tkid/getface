<template>
  <div class="createViewArea materialBox">
    <v-layout>
      <v-flex xs8>
        <span class="mb-2">Название зоны</span>
        <v-text-field hide-details placeholder="Название.." solo></v-text-field>
      </v-flex>
      <v-flex xs4 d-flex align-end>
        <v-btn class="ma-0 ml-2" outline color="gray" @click="checkAll(true)">
          <span v-if="checkFlag">Снять все</span>
          <span v-else>Отметить все</span>
          </v-btn>
      </v-flex>
    </v-layout>
    <v-layout class="mt-2">
      <v-flex>
        <span>Список камер</span>
        <ul class="modalCameraList">
          <li v-for="(camera,i) in cameras" :key="i">
            <input type="checkbox" :id="'camera'+ i" v-model="camera.checked">
            <label :for="'camera'+ i">{{camera.name}}</label>
          </li>
        </ul>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex>
        <v-btn color="primary">Сохранить</v-btn>
      </v-flex>
    </v-layout>
  </div>
</template>
<script>
export default {
  data(){
    return {
      checkFlag: false,
      cameras: [
        {
          name: 'Камера 1',
          checked: false
        },
        {
          name: 'Камера 2',
          checked: false
        },
        {
          name: 'Камера 3',
          checked: false
        },
        {
          name: 'Камера 4',
          checked: false
        },
        {
          name: 'Камера 5',
          checked: false
        },
        {
          name: 'Камера 6',
          checked: false
        },
        {
          name: 'Камера 7',
          checked: false
        },
        {
          name: 'Камера 8',
          checked: false
        },
      ]
    }
  },
  methods: {
    checkAll(){
      let arr = this.cameras;
      this.checkFlag = !this.checkFlag
      arr.forEach((elem,i) => {
        elem.checked = !elem.checked;
      })
    }
  }
};
</script>
<style scoped>
.createViewArea {
  position: absolute;
  top: 45px;
  right: 0;
  z-index: 999;
  padding: 20px;
  width: 400px;
}
.modalCameraList {
  list-style: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
}
.modalCameraList li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 5px;
}
.modalCameraList li input {
  width: 20px;
  height: 20px;
  margin-right: 10px;
}
</style>
