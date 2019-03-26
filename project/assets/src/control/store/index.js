import Vue from 'vue'
import Vuex from 'vuex'
import Auth from './auth'
import V1 from './api_v1'
import Session from './session'

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        session: Session,
        auth: Auth,
        v1: V1,
    },
    state: {},
    mutations: {},
    actions: {}
});
