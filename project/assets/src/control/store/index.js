import Vue from 'vue'
import Vuex from 'vuex'
import Auth from './auth'
import V1 from './api_v1'
import Analitic from './analitic'
import Home from './home'

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        auth: Auth,
        v1: V1,
        Analitic,
        Home
    },
    state: {},
    mutations: {},
    actions: {}
});
