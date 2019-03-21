<template>
  <div>
    <div class="mainStat-row">
      <div class="checkBoxContainer statCommon">
        <input class="check" type="checkbox" name="violation1" id="violation1">
      </div>
      <div class="statCheckbox statCommon" @click="openSelect">
        Мужчины до 18
        <span class="selectArrow">⌵</span>
        <div class="customSelect statCommon">
          <ul>
            <li>
              <input class="check" type="checkbox">
              <label for>Мужчины до 18</label>
            </li>
            <li>
              <input class="check" type="checkbox">
              <label for>Мужчины до 18</label>
            </li>
            <li>
              <input class="check" type="checkbox">
              <label for>Мужчины до 18</label>
            </li>
          </ul>
        </div>
      </div>
      <div class="statTotal statCommon">45</div>
    </div>
    <div class="mainStat-row">
      <div class="checkBoxContainer statCommon">
        <input class="check" type="checkbox" name="violation2" id="violation2">
      </div>
      <div class="statCheckbox statCommon" @click="openSelect">
        Мужчины до 18
        <span class="selectArrow">⌵</span>
        <div class="customSelect statCommon">
          <ul>
            <li>
              <input class="check" type="checkbox">
              <label for>Мужчины до 18</label>
            </li>
            <li>
              <input class="check" type="checkbox">
              <label for>Мужчины до 18</label>
            </li>
            <li>
              <input class="check" type="checkbox">
              <label for>Мужчины до 18</label>
            </li>
          </ul>
        </div>
      </div>
      <div class="statTotal statCommon">45</div>
    </div>
    <div class="mainStat-row">
      <div class="checkBoxContainer statCommon">
        <input class="check" type="checkbox" name="violation3" id="violation3">
      </div>
      <div class="statCheckbox statCommon" @click="openSelect">
        Мужчины до 18
        <span class="selectArrow">⌵</span>
        <div class="customSelect statCommon">
          <ul>
            <li>
              <input class="check" type="checkbox">
              <label for>Мужчины до 18</label>
            </li>
            <li>
              <input class="check" type="checkbox">
              <label for>Мужчины до 18</label>
            </li>
            <li>
              <input class="check" type="checkbox">
              <label for>Мужчины до 18</label>
            </li>
          </ul>
        </div>
      </div>
      <div class="statTotal statCommon">45</div>
    </div>
    <div class="mainStat-row">
      <div class="checkBoxContainer statCommon">
        <input class="check" type="checkbox" name="violation4" id="violation4">
      </div>
      <div class="statCheckbox statCommon" @click="openSelect">
        Мужчины до 18
        <span class="selectArrow">⌵</span>
        <div class="customSelect statCommon">
          <ul>
            <li>
              <input class="check" type="checkbox">
              <label for>Мужчины до 18</label>
            </li>
            <li>
              <input class="check" type="checkbox">
              <label for>Мужчины до 18</label>
            </li>
            <li>
              <input class="check" type="checkbox">
              <label for>Мужчины до 18</label>
            </li>
          </ul>
        </div>
      </div>
      <div class="statTotal statCommon">45</div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
  methods: {
    openSelect(e) {
      if (e.target.classList.contains("statCheckbox")) {
        e.target.querySelector(".customSelect").classList.toggle("show");
      }
    }
  }
};
</script>
<style scoped>
.mainStat-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 3px;
}

.checkBoxContainer {
  width: 50px;
}

.statCheckbox {
  flex: 5;
  position: relative;
}
.check {
  height: 20px;
  width: 20px;
  position: relative;
}

.check:after {
  content: "\00D7";
  display: block;
  background: white;
  pointer-events: none;
  font-size: 15px;
  position: absolute;
  top: 0;
  left: 0;
  height: 20px;
  width: 20px;
  color: transparent;
  transition: 0.25s all;
  border-radius: 3px;
  line-height: 15px;
  background-position: 0 15px;
  background-repeat: no-repeat;
  background-size: 15px 15px;
  border-color: #ccc;
  border-width: 2px;
  border-style: solid;
}
.check:before {
  content: "⅃";
  position: absolute;
  color: #fff;
  top: -1px;
  left: 6px;
  font-weight: bold;
  transform: rotate(45deg);
  z-index: 999;
}
.check:checked:after {
  background-color: #7d6df2;
  border-color: #7d6df2;
}
.check:hover:after {
  border-color: #7d6df2;
}

.statTotal {
  flex: 2;
}

.statCommon {
  background-color: #fff;
  border: 1px solid #d4d4d4;
  height: 46px;
  border-radius: 3px;
  margin-right: 3px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.statCheckbox {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}
.customSelect {
  display: none;
  position: absolute;
  width: 100%;
  top: 46px;
  z-index: 999;
  height: fit-content;
}
.customSelect ul {
  list-style: none;
  padding: 0;
  width: 100%;
}
.customSelect ul li {
  display: flex;
  justify-content: space-around;
  padding: 10px;
}
.selectArrow {
  margin-left: 10px;
  margin-bottom: 5px;
  font-size: 20px;
  font-weight: bold;
}
.show {
  display: block;
}
</style>


