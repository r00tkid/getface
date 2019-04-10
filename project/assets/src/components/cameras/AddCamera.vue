<template>
  <div class="createCamera-modal materialBox">
    <v-layout>
      <v-flex>
        <v-layout class="mb-2">
          <v-flex xs5>
            <span>Название камеры:</span>
          </v-flex>
          <v-flex xs7>
            <v-text-field hide-details v-model="cameraModal.name" solo></v-text-field>
          </v-flex>
        </v-layout>
        <v-layout class="mb-2">
          <v-flex xs5>
            <span>API ключ:</span>
          </v-flex>
          <v-flex xs7>
            <v-text-field hide-details v-model="cameraModal.key" solo></v-text-field>
          </v-flex>
        </v-layout>
        <v-layout class="mb-3">
          <v-flex xs5>
            <span>Статус:</span>
          </v-flex>
          <v-flex xs7>
            <v-text-field hide-details v-model="cameraModal.status" solo></v-text-field>
          </v-flex>
        </v-layout>
        <v-layout class="mb-2">
          <v-flex xs6>
            <v-btn class="ma-0" dark color="get-orange">
              Проверьте зону
              <br>видимости камеры
            </v-btn>
          </v-flex>
          <v-flex xs6>
            <div class="cameraMask materialBox">
              <img src="@/assets/video.svg" alt="camera">
            </div>
          </v-flex>
        </v-layout>
        <v-layout>
          <v-flex xs7>
            <v-btn dark color="primary">Сохранить/Редактировать</v-btn>
          </v-flex>
          <v-flex xs5>
            <v-btn dark color="#fa6d6e">Удалить камеру</v-btn>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </div>
</template>
<script>
export default {
  data() {
    return {
      cameraModal: {
        name: "Camera 1",
        key: "12234324534534564",
        status: "Conected"
      }
    };
  }
};
</script>
<style scoped>
.createCamera-modal {
  position: absolute;
  top: 45px;
  left: 7px;
  z-index: 999;
  padding: 20px;
}
.cameraMask {
  height: 150px;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.cameraMask img {
  width: 60px;
  height: auto;
}
</style>
