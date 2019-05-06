<template>
    <div>
        <div v-for="(item,i) in items" :key="i" class="mainStat-row">
            <div class="checkBoxContainer statCommon">
                <input @click="changeChart(i)" v-model="item.checked" class="check" type="checkbox" :name="'violation'+ i" :id="'violation'+ i">
            </div>
            <template v-if="item.subitems">
                <div
                        class="statCheckbox statCommon"
                        :style="{borderColor: colors[i]}"
                        :data-id="i"
                        @click="openSelect"
                >
                    {{item.name}}
                    <i :data-id="i" v-if="!openedSelects[i]" class="material-icons">arrow_drop_down</i>
                    <i :data-id="i" v-else class="material-icons">arrow_drop_up</i>
                    <div v-show="openedSelects[i]" class="customSelect statCommon">
                        <ul>
                            <li v-for="(subitem,i) in item.subitems" :key="i">
                                <input v-model="subitem.checked" class="check" type="checkbox">
                                <label>{{subitem.name}}</label>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="statTotal statCommon">45</div>
            </template>
            <template v-else>
                <label :for="'violation'+ i" class="statCheckbox statCommon" :style="{borderColor: colors[i]}">{{ item.name }}</label>
                <div class="statTotal statCommon">{{item.val}}</div>
            </template>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            colors: {
                type: Array,
                required: true
            },
            items: {
                type: Array,
                required: true
            }
        },
        data() {
            return {
                openedSelects: [false, false],
            };
        },
        methods: {
            openSelect(e) {
                let id = e.target.getAttribute("data-id");
                this.$set(this.openedSelects, id, !this.openedSelects[id]);
            },
            changeChart(i) {
                this.$bus.$emit('toggleChart', i);
            }
        },
        computed: {
            activeChartLine() {
                return this.$store.getters.getActiveChartLine;
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