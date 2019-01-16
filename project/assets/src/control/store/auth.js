import Vue from 'vue'

const Auth = {
    namespaced: true,
    state: {
        authenticated: false,
        user: {},
        token: ''
    },
    mutations: {
        setAuth(state, value) {
            state.authenticated = value;
        },
        setUser(state, value) {
            state.user = value
        },
        setToken(state, value) {
            state.token = value.token;
            value.remember ? localStorage.setItem('token', value.token) : sessionStorage.setItem('token', value.token);
            Vue.prototype.axios.defaults.headers.common['Authorization'] = `Bearer ${value.token}`;
        },
        purgeToken(state) {
            state.token = '';
            localStorage.removeItem('token');
            sessionStorage.removeItem('token');
        },
        purgeUser(state) {
            state.user = {}
        },
        purgeAuth(state) {
            state.authenticated = false;
            delete Vue.prototype.axios.defaults.headers.common['Authorization'];

        }
    },
    actions: {
        login: ({commit, state, dispatch}, data) => {
            return Vue.prototype.axios.post('auth/sign-in', data).then(res => {
                const token = res.data.token;
                commit('setToken', {token: data.token, remember: data.remember_me});
                dispatch('retrieveUser');
                return res;
            }).catch(e => {
                throw e;
            });
        },
        retrieveUser: ({commit}) => {
            return new Promise((resolve, reject) => {
                Vue.prototype.axios.get('auth/me').then(res => {
                    commit('setUser', res.data.user);
                    commit('setAuth', true);
                    resolve(res)
                }).catch(e => {
                    commit('purgeToken');
                    reject(e)
                })
            });
        },
        logout: ({commit}) => {
            return new Promise((resolve) => {
                commit('purgeToken');
                commit('purgeUser');
                commit('purgeAuth');
                resolve(true);
            });
        },
        register: ({commit, dispatch}, data) => {
            return new Promise((resolve, reject) => {
                Vue.prototype.axios.post('auth/sign-up', data).then(res => {
                    const token = res.data.token;
                    commit('setToken', {token: token, remember: true});
                    dispatch('retrieveUser');
                    resolve(res)
                }, err => {
                    reject(err);
                }).catch(e => {
                    reject(e);
                })
            });
        }
    },
    getters: {
        user: state => {
            return state.user;
        },
        isAuth: state => {
            return state.authenticated;
        }
    }
};

export default Auth;
