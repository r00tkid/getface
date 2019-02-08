<template>
  <div class="orangeBox get-orange">
    <div class="orangeBox-item">
      <div>
        <p class="orangeStart get-orange">
          <span>Начало</span>
          <span>03.12.18</span>
        </p>
        <p class="orangeLeft">
          <span>Начало</span>
          <span>03.12.18</span>
        </p>
      </div>
    </div>
    <div class="orangeBox-item">
      <div>
        <p class="orangeStart get-orange">
          <span>Начало</span>
          <span>03.12.18</span>
        </p>
        <p class="orangeLeft">
          <span>Начало</span>
          <span>03.12.18</span>
        </p>
      </div>
    </div>
    <div class="orangeBox-item">
      <v-icon dark class>add_circle</v-icon>
    </div>
    <div class="orangeBox-item">
      <v-icon dark class>add_circle</v-icon>
    </div>
    <div class="orangeBox-item">
      <v-icon dark class>add_circle</v-icon>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
.orangeBox{
    display: flex;
    padding: 5px 10px;
    justify-content: space-between;
    border-radius: 5px;
    box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
    0 1px 5px 0 rgba(0, 0, 0, 0.12);
    padding: 10px;
}
.orangeBox-item{
    flex: 1;
    margin: 0 5px;
    border: 1px solid #fff;
    border-radius: 4px;
    width: 60px;
    height: 60px;
    background-color: rgba(256, 256, 256, 0.2);
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    overflow: hidden;
}
.orangeBox-item div{
    padding: 1px;
    width: 100%;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    font-size: 10px;
}
.orangeBox-item div p{
    margin: 0;
    flex: 1;
    display: flex;
    flex-direction: column;
    line-height: 14px;
}
.orangeBox-item div p span:last-child{
    font-weight: bold;
}
.orangeBox-item div .orangeStart{
    color: #fff;
    border-radius: 4px;
}
</style>


