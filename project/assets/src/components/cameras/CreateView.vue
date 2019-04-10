<template>
  <div class="createViewArea materialBox">
    <v-layout>
      <v-flex xs6>
        <span class="mb-2">Название зоны</span>
        <v-text-field hide-details placeholder="Название.." solo></v-text-field>
      </v-flex>
      <v-flex xs6 d-flex align-end>
        <v-btn class="ma-0 ml-2" outline small color="gray">Отметить все</v-btn>
        <v-btn class="ma-0 ml-1" outline small color="gray">Снять все</v-btn>
      </v-flex>
    </v-layout>
    <v-layout class="mt-2">
      <v-flex>
        <span>Список камер</span>
        <ul class="modalCameraList">
          <li>
            <input type="checkbox" id="camera1">
            <label for="camera1">Камера 1</label>
          </li>
          <li>
            <input type="checkbox" id="camera2">
            <label for="camera2">Камера 2</label>
          </li>
          <li>
            <input type="checkbox" id="camera3">
            <label for="camera3">Камера 3</label>
          </li>
          <li>
            <input type="checkbox" id="camera4">
            <label for="camera4">Камера 4</label>
          </li>
          <li>
            <input type="checkbox" id="camera5">
            <label for="camera5">Камера 5</label>
          </li>
        </ul>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex>
        <v-btn class="mr-2 ml-0" outline color="gray">Удалить</v-btn>
        <v-btn color="primary">Сохранить</v-btn>
      </v-flex>
    </v-layout>
  </div>
</template>
<script>
export default {};
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
