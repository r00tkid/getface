<template>
    <div>
        <div class="mainStat-row">
            <div class="checkBoxContainer statCommon">
                <input class="check" type="checkbox" name="violation1" id="violation1">
            </div>
            <div
                    class="statCheckbox statCommon"
                    :style="{borderColor: colors[0]}"
                    data-id="0"
                    @click="openSelect"
            >
                Мужчины до 18
                <i v-if="!openedSelects[0]" class="material-icons">arrow_drop_down</i>
                <i v-else class="material-icons">arrow_drop_up</i>
                <div v-show="openedSelects[0]" class="customSelect statCommon">
                    <ul>
                        <li>
                            <input class="check" type="checkbox" id="mySelect1">
                            <label for="mySelect1">Мужчины до 18</label>
                        </li>
                        <li>
                            <input class="check" type="checkbox" id="mySelect2">
                            <label for="mySelect2">Мужчины до 18</label>
                        </li>
                        <li>
                            <input class="check" type="checkbox" id="mySelect3">
                            <label for="mySelect3">Мужчины до 18</label>
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
            <div
                    class="statCheckbox statCommon"
                    :style="{borderColor: colors[1]}"
                    data-id="1"
                    @click="openSelect"
            >
                Женщины до 18
                <i v-if="!openedSelects[1]" class="material-icons">arrow_drop_down</i>
                <i v-else class="material-icons">arrow_drop_up</i>
                <div v-show="openedSelects[1]" class="customSelect statCommon">
                    <ul>
                        <li>
                            <input class="check" type="checkbox" id="mySelect4">
                            <label for="mySelect4">Женщины до 18</label>
                        </li>
                        <li>
                            <input class="check" type="checkbox" id="mySelect5">
                            <label for="mySelect5">Женщины до 18</label>
                        </li>
                        <li>
                            <input class="check" type="checkbox" id="mySelect6">
                            <label for="mySelect6">Женщины до 18</label>
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
            <div class="statCheckbox statCommon" :style="{borderColor: colors[2]}">Среднее время</div>
            <div class="statTotal statCommon">45</div>
        </div>
        <div class="mainStat-row">
            <div class="checkBoxContainer statCommon">
                <input class="check" type="checkbox" name="violation4" id="violation4">
            </div>
            <div class="statCheckbox statCommon" :style="{borderColor: colors[3]}">Количество посещений</div>
            <div class="statTotal statCommon">45</div>
        </div>
        <div class="mainStat-row">
            <div class="checkBoxContainer statCommon">
                <input class="check" type="checkbox" name="violation4" id="violation4">
            </div>
            <div class="statCheckbox statCommon" :style="{borderColor: colors[4]}">Чеки</div>
            <div class="statTotal statCommon">45</div>
        </div>
        <div class="mainStat-row">
            <div class="checkBoxContainer statCommon">
                <input class="check" type="checkbox" name="violation4" id="violation4">
            </div>
            <div class="statCheckbox statCommon" :style="{borderColor: colors[5]}">Конверсия</div>
            <div class="statTotal statCommon">45</div>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            colors: {
                type: Array,
                required: true
            }
        },
        data() {
            return {
                openedSelects: [false, false, false, false]
            };
        },
        methods: {
            openSelect(e) {
                let id = e.target.getAttribute("data-id");
                this.$set(this.openedSelects, id, !this.openedSelects[id]);
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
        text-align: center;
    }

    .customSelect {
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

    .transformArrow {
        transform: rotate(180deg);
    }
</style>