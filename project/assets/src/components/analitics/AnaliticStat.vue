<template>
    <div>
        <div class="mainStat-row">
            <div class="checkBoxContainer statCommon"></div>
            <div class="statCheckbox statCommon">
                <input type="checkbox" name="violation1" id="violation1">
                <label for="violation1">Нарушений</label>
            </div>
            <div class="statTotal statCommon">45</div>
        </div>
        <div class="mainStat-row">
            <div class="checkBoxContainer statCommon"></div>
            <div class="statCheckbox statCommon">
                <input type="checkbox" name="violation2" id="violation2">
                <label for="violation2">Опозданий</label>
            </div>
            <div class="statTotal statCommon">45</div>
        </div>
        <div class="mainStat-row">
            <div class="checkBoxContainer statCommon"></div>
            <div class="statCheckbox statCommon">
                <input type="checkbox" name="violation3" id="violation3">
                <label for="violation3">Ушёл раньше</label>
            </div>
            <div class="statTotal statCommon">45</div>
        </div>
        <div class="mainStat-row">
            <div class="checkBoxContainer statCommon"></div>
            <div class="statCheckbox statCommon">
                <input type="checkbox" name="violation4" id="violation4">
                <label for="violation4">Разница часов</label>
            </div>
            <div class="statTotal statCommon">45</div>
        </div>
    </div>
</template>
<script>
    export default {};
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

    .statCheckbox input[type="checkbox"] + label:before {
        border: 2px solid #7d6df2;
        content: "\00a0";
        display: inline-block;
        height: 20px;
        width: 20px;
        margin: 0 0.25em 0 0;
        padding: 0;
        border-radius: 3px;
        vertical-align: top;
        position: absolute;
        left: -39px;
    }

    .statCheckbox input[type="checkbox"]:checked + label:before {
        background: linear-gradient(
                to right top,
                #7d6df2,
                #9077f4,
                #a181f6,
                #b08bf9,
                #be96fb
        );
        text-align: center;
    }

    .statCheckbox input[type="checkbox"]:checked + label:after {
        font-weight: bold;
        content: "⅃";
        position: absolute;
        transform: rotate(45deg);
        left: -33px;
        top: 9px;
        font-size: 16px;
        color: #fff;
    }

    .statCheckbox input[type="checkbox"]:focus + label::before {
        outline: rgb(59, 153, 252) auto 5px;
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

    .statCheckbox input[type="checkbox"] {
        visibility: hidden;
    }

    .statCheckbox {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .statCheckbox label {
        cursor: pointer;
    }
</style>


