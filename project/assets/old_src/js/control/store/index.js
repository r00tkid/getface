import Vue from 'vue';
import Vuex from 'vuex';

import Api from './api';
import Tech from './tech';
import Tests from './tests'

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        api: Api,
        tech: Tech,
        tests: Tests,
    },
    state: {},
    mutations: {},
    actions: {}
});