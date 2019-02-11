import Vue from 'vue'
import Vuex from 'vuex'
import Modal from './modal'
import Auth from './auth'

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        modal: Modal,
        auth: Auth
    },
    state: {},
    mutations: {},
    actions: {}
});
