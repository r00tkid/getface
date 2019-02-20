import Vue from 'vue'
import Vuex from 'vuex'
import Modal from './modal'
import Auth from './auth'
import V1 from './api_v1'

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        modal: Modal,
        auth: Auth,
        v1: V1,
    },
    state: {},
    mutations: {},
    actions: {}
});
