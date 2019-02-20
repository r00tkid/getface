import router from './router'
import store from "./store";
import Vue from "vue";

const http = require('axios').default;

http.interceptors.request.use(request => {
    request.headers.common['Accept'] = "application\/json";
    let token;

    if ((token = sessionStorage.getItem('token') || localStorage.getItem('token'))) {
        request.headers.common['Authorization'] = `Bearer ${token}`;
    }

    return request;
});

/**
 * @type {AxiosInstance}
 */
Vue.prototype.$http = function (route_name, data = undefined, type = 'get', api_version = 1, headers = {}, override_params = undefined, uri = undefined, responseType = undefined) {
    let request_url = null;

    if (uri)
        request_url = uri;
    else
        request_url = store.getters[`v${api_version}/uri`](route_name);

    let params = {
        method: type,
        url: request_url,
        headers: headers,
    };

    data && (params.data = data);
    responseType && (params.responseType = responseType);

    if (override_params && "object" == typeof override_params) {
        for (let param in override_params) {
            params[param] = override_params[param];
        }
    }

    return http(params)
        .catch(e => {
            if (e.response && e.response.status === 401) {
                router.push({name: "landing"});
            }

            throw e;
        });
};

Vue.prototype.$axios = http;

export default http;