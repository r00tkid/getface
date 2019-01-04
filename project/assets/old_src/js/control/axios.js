import Vue from 'vue';
import axios from 'axios';

const http = axios;
Vue.prototype.$http = http;

http.interceptors.request.use(request => {
    request.headers.common['Accept'] = "application\/json";
    let token;

    if ((token = localStorage.getItem('auth-token'))) {
        request.headers.common['Authorization'] = token;
    }

    return request
});

export default http;