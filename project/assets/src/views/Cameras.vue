<template>
    <v-container @click="closeAll($event)" fluid class="cameraPageContainer">
        <v-layout>
            <v-flex class="createCamera-box" lg6>
                <v-btn color="primary" @click.stop="isCameraModal = !isCameraModal">
                    <v-icon class="mr-2">add_circle</v-icon>
                    Добавить камеру
                </v-btn>
                <v-btn outline color="gray">Статистика</v-btn>
                <div v-show="isCameraModal" @click.stop="stopProp($event)">
                    <add-camera></add-camera>
                </div>
            </v-flex>
            <v-flex lg6 class="changeViewContainer">
                <v-btn @click.stop="isCreateViewModal = !isCreateViewModal" dark color="get-orange">
                    <v-icon class="mr-2">add_circle</v-icon>
                    Создать зону видимости
                </v-btn>
                <v-btn outline color="gray" @click="hideViews = !hideViews">Вид</v-btn>
                <transition name="fade">
                    <div v-show="!hideViews" class="viewHiddenBox" @click="changeViewGrid">
                        <div class="viewHiddenBox-item">
                            <img src="@/assets/images/1.png" draggable="false" data-imgnum="1" alt="gridIcon">
                        </div>
                        <div class="viewHiddenBox-item">
                            <img src="@/assets/images/2.png" draggable="false" data-imgnum="2" alt="gridIcon">
                        </div>
                        <div class="viewHiddenBox-item">
                            <img src="@/assets/images/3.png" draggable="false" data-imgnum="3" alt="gridIcon">
                        </div>
                        <div class="viewHiddenBox-item">
                            <img src="@/assets/images/4.png" draggable="false" data-imgnum="4" alt="gridIcon">
                        </div>
                        <div class="viewHiddenBox-item">
                            <img src="@/assets/images/5.png" draggable="false" data-imgnum="5" alt="gridIcon">
                        </div>
                        <div class="viewHiddenBox-item">
                            <img src="@/assets/images/6.png" draggable="false" data-imgnum="6" alt="gridIcon">
                        </div>
                        <div class="viewHiddenBox-item">
                            <img src="@/assets/images/7.png" draggable="false" data-imgnum="7" alt="gridIcon">
                        </div>
                        <div class="viewHiddenBox-item">
                            <img src="@/assets/images/8.png" draggable="false" data-imgnum="8" alt="gridIcon">
                        </div>
                        <div class="viewHiddenBox-item">
                            <img src="@/assets/images/9.png" draggable="false" data-imgnum="9" alt="gridIcon">
                        </div>
                    </div>
                </transition>
                <div v-show="isCreateViewModal" @click.stop="stopProp($event)">
                    <create-view></create-view>
                </div>
            </v-flex>
        </v-layout>
        <v-layout class="mt-2">
            <v-flex lg3 d-flex class="camerasListContainer">
                <div class="camerasList">
                    <div class="searchCamera">
                        <v-text-field hide-details label="Search" solo></v-text-field>
                        <v-btn class="ma-0" color="primary">
                            <v-icon>search</v-icon>
                        </v-btn>
                    </div>
                    <div class="videoListBox"></div>
                    <div class="videoListBox"></div>
                    <div class="videoListBox"></div>
                    <div class="videoListBox"></div>
                    <div class="videoListBox"></div>
                </div>
            </v-flex>
            <v-flex lg9 class="pl-2">
                <div class="videoGrid" :class="activeView">
                    <template v-for="(camera, i) in cameras">
                        <div :key="i" :class="{'videoGrid-item--first':  i == 0, 'videoGrid-item--second':  i == 1}" class="videoGrid-item">
                            <div class="cameraOverlay">
                                <div class="cameraOverlay-top">
                                    <div>
                                        <h4>Camera №{{camera.id + 1}}</h4>
                                        <v-icon class="removeCamera">close</v-icon>
                                    </div>
                                </div>
                                <div class="cameraOverlay-bottom">
                                    <v-btn color="primary">Изменить</v-btn>
                                    <v-btn color="primary">
                                        <v-icon>zoom_out_map</v-icon>
                                    </v-btn>
                                </div>
                            </div>
                        </div>
                    </template>
                </div>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import AddCamera from "../components/cameras/AddCamera";
    import CreateView from "../components/cameras/CreateView";

    export default {
        components: {
            AddCamera,
            CreateView
        },
        name: "Cameras",
        data() {
            return {
                class: 1,
                hideViews: true,
                isCameraModal: false,
                isCreateViewModal: false,
                cameras: [
                    {
                        id: 0
                    },
                    {
                        id: 1
                    },
                    {
                        id: 2
                    },
                    {
                        id: 3
                    },
                    {
                        id: 4
                    },
                    {
                        id: 5
                    },
                    {
                        id: 6
                    },
                    {
                        id: 7
                    },
                    {
                        id: 8
                    },
                    {
                        id: 9
                    },
                    {
                        id: 10
                    },
                    {
                        id: 11
                    }
                ]
            };
        },
        methods: {
            changeViewGrid(e) {
                this.class = e.target.dataset.imgnum;
            },
            closeAll(e) {
                this.isCreateViewModal = false;
                this.isCameraModal = false;
            },
            stopProp(e) {
            }
        },
        computed: {
            activeView() {
                return "view" + this.class;
            }
        }
    };
</script>

<style>
    .changeViewContainer {
        display: flex;
        justify-content: flex-end;
        position: relative;
    }

    .fade-enter-active,
    .fade-leave-active {
        transition: opacity 0.3s;
    }

    .fade-enter,
    .fade-leave-to {
        opacity: 0;
    }

    .v-text-field.v-text-field--solo .v-input__control {
        min-height: 35px;
    }

    .cameraPageContainer {
        width: 80%;
    }

    .camerasListContainer {
        padding: 10px;
        background-color: #fff;
        box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.2), 0 4px 5px 0 rgba(0, 0, 0, 0.14),
        0 1px 10px 0 rgba(0, 0, 0, 0.12);
        border-radius: 4px;
        border: 1px solid #d4d4d4;
        position: relative;
    }

    .camerasListContainer:before {
        content: "";
        position: absolute;
        width: 1px;
        height: 100%;
        background-color: #d4d4d4;
        right: 26px;
        top: 0;
    }

    .createCamera-box {
        position: relative;
    }

    .viewHiddenBox {
        position: absolute;
        right: 8px;
        bottom: -210px;
        padding: 10px;
        background-color: #fff;
        box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.2), 0 4px 5px 0 rgba(0, 0, 0, 0.14),
        0 1px 10px 0 rgba(0, 0, 0, 0.12);
        border-radius: 4px;
        border: 1px solid #d4d4d4;
        z-index: 999;
        width: 250px;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-rows: 33% 33% 33%;
        grid-auto-rows: 33%;
    }

    .viewHiddenBox-item {
        min-height: 50px;
        margin: 5px;
    }

    .viewHiddenBox-item img {
        width: 100%;
        height: 100%;
        transition: 0.3s;
    }

    .viewHiddenBox-item :hover {
        transform: scale(1.1);
    }

    .camerasList {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 0px 20px 0px 0px;
        max-height: 700px;
        overflow-y: scroll;
    }

    .camerasList .v-btn {
        min-width: 60px;
    }

    ::-webkit-scrollbar-track {
        -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
        border-radius: 10px;
        background-color: #f5f5f5;
    }

    ::-webkit-scrollbar {
        width: 6px;
        background-color: #f5f5f5;
    }

    ::-webkit-scrollbar-thumb {
        border-radius: 10px;
        -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
        background-color: #969696;
    }

    .searchCamera {
        display: flex;
        min-height: 50px;
    }

    .searchCamera button {
        height: 40px;
    }

    .videoListBox {
        min-height: 150px;
        width: 100%;
        background-color: #ccc;
        margin-bottom: 5px;
    }

    .videoGrid {
        width: 100%;
        height: 100%;
        padding: 10px;
        background-color: #fff;
        box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.2), 0 4px 5px 0 rgba(0, 0, 0, 0.14),
        0 1px 10px 0 rgba(0, 0, 0, 0.12);
        border-radius: 4px;
        border: 1px solid #d4d4d4;
        position: relative;
        max-height: 722px;
        overflow-y: auto;
        display: grid;
        grid-gap: 10px;
        overflow-x: hidden;
    }

    .videoGrid-item {
        background-color: #ccc;
        position: relative;
    }

    .cameraOverlay {
        position: absolute;
        width: 100%;
        height: 100%;
        opacity: 0;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.3s;
    }

    .cameraOverlay:hover {
        opacity: 1;
    }

    .cameraOverlay-bottom {
        display: flex;
        justify-content: space-between;
    }

    .cameraOverlay-top {
        display: flex;
        position: relative;
        text-align: center;
        justify-content: center;
        padding: 10px 0;
        background-color: rgba(256, 256, 256, 0.6);
    }

    .removeCamera {
        position: absolute;
        right: 10px;
        top: 10px;
        color: red !important;
        cursor: pointer;
    }

    .view1 {
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 50% 50%;
        grid-auto-rows: 50%;
    }

    .view2 {
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-rows: 50% 50%;
        grid-auto-rows: 50%;
    }

    .view3 {
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-rows: 33% 33% 33%;
        grid-auto-rows: 33%;
    }

    .view4 {
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-rows: 33% 33% 33%;
        grid-auto-rows: 33%;
    }

    .view4 .videoGrid-item--first {
        grid-column-start: 1;
        grid-column-end: 3;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .view5 {
        grid-template-columns: 1fr 1fr 1fr 1fr;
        grid-template-rows: 33% 33% 33%;
        grid-auto-rows: 33%;
    }

    .view5 .videoGrid-item--first {
        grid-column-start: 1;
        grid-column-end: 3;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .view5 .videoGrid-item--second {
        grid-column-start: 3;
        grid-column-end: 5;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .view6 {
        grid-template-columns: 1fr 1fr 1fr 1fr;
        grid-template-rows: 25% 25% 25% 25%;
        grid-auto-rows: 25%;
    }

    .view6 .videoGrid-item--first {
        grid-column-start: 1;
        grid-column-end: 3;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .view6 .videoGrid-item--second {
        grid-column-start: 3;
        grid-column-end: 5;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .view7 {
        grid-template-columns: 1fr 1fr 1fr 1fr;
        grid-template-rows: 25% 25% 25% 25%;
        grid-auto-rows: 25%;
    }

    .view7 .videoGrid-item--first {
        grid-column-start: 2;
        grid-column-end: 4;
        grid-row-start: 2;
        grid-row-end: 4;
    }

    .view8 {
        grid-template-columns: 1fr 1fr 1fr 1fr;
        grid-template-rows: 25% 25% 25% 25%;
        grid-auto-rows: 25%;
    }

    .view8 .videoGrid-item--first {
        grid-column-start: 1;
        grid-column-end: 4;
        grid-row-start: 1;
        grid-row-end: 4;
    }

    .view9 {
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
        grid-template-rows: 16% 16% 16% 16% 16% 16%;
        grid-auto-rows: 16%;
    }

    .view9 .videoGrid-item--first {
        grid-column-start: 1;
        grid-column-end: 6;
        grid-row-start: 1;
        grid-row-end: 6;
    }
</style>