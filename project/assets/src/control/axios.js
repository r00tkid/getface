import axios from "axios";
import store from "./store";
import router from "./router";
import Vue from "vue";

const http = axios.create({
    baseURL: 'http://192.168.1.254:9090/api/v1/',
    headers: {
        'Accept': "application\/json"
    }
    // timeout: 2000,
});

/**
 * @type {AxiosInstance}
 */
Vue.prototype.axios = http;
if (localStorage.token || sessionStorage.token) {
    const token = localStorage.token || sessionStorage.token;
    http.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    // Only for dev
    store.dispatch('auth/retrieveUser').catch(() => router.push('login'));
}

export default http;