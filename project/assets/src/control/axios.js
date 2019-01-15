import axios from "axios";
import store from "./store";
import router from "./router";
import Vue from "vue";

const http = axios.create({
    baseURL: '/api/v1/',
    headers: {
        'Accept': "application\/json"
    }
    // timeout: 2000,
});

/**
 * @type {AxiosInstance}
 */
Vue.prototype.axios = http;
if (localStorage.token) {
    http.defaults.headers.common['Authorization'] = `Bearer ${localStorage.token}`;
    // Only for dev
    store.dispatch('auth/retrieveUser').catch(() => router.push('login'));
}

export default http;