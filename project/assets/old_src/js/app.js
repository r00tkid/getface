import '@babel/polyfill'
import Vue from 'vue'
import '$dept/head'
import '$dept/axios'
// import '$dept/cookie'
import '$dept/noty'
import '$dept/bus'
import '$plug/vuetify'

import Master from '$view/layout/Master'
import router from '$dept/router'
import store from '$dept/store'

window.Vue = Vue;

// Set to false when done
Vue.config.productionTip = true;

const app = new Vue({
    router,
    store,
    render: h => h(Master)
}).$mount('#app');
