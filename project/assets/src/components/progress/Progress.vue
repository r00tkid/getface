<template>
    <div class="progressContainer">
        <h4>Количество вне зоны видимости</h4>
        <div class="progressBox">
            <div class="timeProgressBar">
                <span class="progressPoint"></span>
                <span class="progressPoint"></span>
                <span class="progressPoint missed"></span>
                <span class="progressPoint missed"></span>
                <span class="progressPoint"></span>
                <span class="progressPoint missed"></span>
                <span class="progressPoint"></span>
                <span class="progressPoint"></span>
                <span class="progressPoint missed"></span>
                <span class="progressPoint"></span>
            </div>
            <div class="timeSum">
                <span>0ч:40м</span>
                <span>6ч:35м</span>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {}
        }
    }
</script>
<style scoped>
    .progressContainer {
        background-color: #fff;
        border: #d4d4d4 solid 1px;
        box-shadow: 0 3px 1px -2px rgba(0, 0, 0, .2), 0 2px 2px 0 rgba(0, 0, 0, .14), 0 1px 5px 0 rgba(0, 0, 0, .12);
        border-radius: 5px;
        padding: 10px;
    }

    .timeProgressBar {
        width: 100%;
        height: 10px;
        background-color: #5ae08f;
        border-radius: 5px;
        display: flex;
        overflow: hidden;
    }

    .progressBox {
        display: flex;
        align-items: center;
    }

    .progressPoint {
        min-width: 10px;
        height: 100%;
        background-color: #5ae08f;
        flex: 1;
    }

    .timeSum {
        display: flex;
        flex-direction: column;
        border-left: 1px solid #d4d4d4;
        padding-left: 30px;
        margin-left: 15px;
    }

    .timeSum span {
        position: relative;
    }

    .timeSum span:before {
        position: absolute;
        content: '';
        width: 10px;
        height: 10px;
        background-color: #5ae08f;
        border-radius: 50%;
        top: 5px;
        left: -20px;
    }

    .timeSum span:first-child:before {
        background-color: #fa6d6e;
    }

    .missed {
        background-color: #fa6d6e;
        border-radius: 5px;
    }
</style>


