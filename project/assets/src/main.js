import '@babel/polyfill'
import Vue from 'vue'
import Vuetify from 'vuetify'
import './plugins/vuetify'
import App from './views/layout/App.vue'
import router from './control/router'
import store from './control/store'
import axios from 'axios'
import '@fortawesome/fontawesome-free/css/all.css'

const http = axios.create({
    baseURL: '/api/v1/',
    headers: {
        'Accept': "application\/json"
    }
    // timeout: 2000,
});

/**
 *
 * @type {AxiosInstance}
 */
Vue.prototype.axios = http;
if (localStorage.token) {
    http.defaults.headers.common['Authorization'] = `Bearer ${localStorage.token}`;
    // Only for dev
    store.dispatch('auth/retrieveUser').catch( () => router.push('login'));
}


// http.interceptors.request.use(config => {
//     config.headers.common['Accept'] = "application\/json";
//
//     if (localStorage.token)
//         config.headers.common['Authorization'] = `Bearer ${localStorage.token}`;
//
//     return config;
// }, function (error) {
//     return Promise.reject(error);
// });
/**
 * Sort of auth gate for routes
 */
router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {

        if (localStorage.getItem('token') == null) {
            next({
                path: '/login',
                params: { nextUrl: to.fullPath }

            })
        } else {
            next()
        }
    } else {
        next()
    }
});

import './control/bus'

import VueNoty from 'vuejs-noty'
import 'vuejs-noty/dist/vuejs-noty.css'

Vue.config.productionTip = false;

Vue.use(VueNoty, {
    timeout: 4000,
    progressBar: true,
    layout: 'topCenter',
    theme: 'nest'
});
Vue.use(Vuetify, {
    iconfont: 'fa4'
})
new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
