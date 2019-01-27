import axios from "axios";
import store from "./store";
import router from "./router";
import Vue from "vue";

const digitalocean = 'http://139.59.211.27:9090';
const local = '';

const http = axios.create({
    baseURL: local + '/api/v1/',
    headers: {
        'Accept': "application\/json"
    },
    timeout: 5000,
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