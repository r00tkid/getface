<template>
  <div class="employeeFaceId materialBox">
    <v-flex d-flex row align-baseline>
      <v-text-field
        class="mt-1 normal-border get-danger--text"
        single-line
        flat
        solo
        hide-details
        label="Указать причину увольнения"
        append-icon="add_circle"
        color="get-danger"
      ></v-text-field>
      <v-btn large color="get-danger" class="white--text">Уволить</v-btn>
    </v-flex>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
</style>


