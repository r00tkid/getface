import Vue from 'vue'
import Vuex from 'vuex'
import Modals from './modals'

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        modal: Modals
    },
    state: {},
    mutations: {},
    actions: {}
})
