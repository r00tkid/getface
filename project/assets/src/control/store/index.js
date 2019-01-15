import Vue from 'vue'
import Vuex from 'vuex'
import Modals from './modals'
import Auth from './auth'

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        modal: Modals,
        auth: Auth
    },
    state: {},
    mutations: {},
    actions: {}
});
