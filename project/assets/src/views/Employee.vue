<template>
  <v-container grid-list-md text-xs-center fluid class="home-wrap">
    <v-layout>
      <v-flex xs5>
        <div class="employeeFaceId materialBox">
            <v-layout>
                <v-flex xs6>
                    <v-avatar
                        :size="150"
                        color="grey lighten-4"
                        >
                        <img src="https://vuetifyjs.com/apple-touch-icon-180x180.png" alt="avatar">
                    </v-avatar>
                    <v-btn color="#fa6d6e" dark class="removeID">Удалить Face ID</v-btn>
                </v-flex>
                <v-flex xs6>
                    dfhfghfgj
                </v-flex>
            </v-layout>
        </div>
        <div class="fireEmployee"></div>
        <div class="rewards"></div>
      </v-flex>
      <v-flex xs7></v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
    
};
</script>
<style scoped>
.home-wrap {
  padding: 24px 0;
  width: 80%;
}
.materialBox{
    background-color: #fff;
    border: 1px solid #d4d4d4;
    border-radius: 5px;
    box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
    0 1px 5px 0 rgba(0, 0, 0, 0.12);
    padding: 10px;
}
.removeID{
    margin-top: -15px;
}
</style>


