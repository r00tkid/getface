import $http from './../axios'

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
            $http.defaults.headers.common['Authorization'] = `Bearer ${value.token}`;
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
            delete $http.defaults.headers.common['Authorization'];

        }
    },
    actions: {
        login: ({commit, state, dispatch}, data) => {
            return $http.post('auth/sign-in', data)
                .then(res => {
                    const token = res.data.token;
                    commit('setToken', {token: token, remember: data.remember_me});
                    dispatch('retrieveUser');
                    return res;
                });
        },
        retrieveUser: ({commit, dispatch}) => {
            return $http.get('auth/me')
                .then(res => {
                    commit('setUser', res.data.user);
                    commit('setAuth', true);
                }).catch(e => {
                    // todo Review this
                    try {
                        dispatch('refreshToken').then(res => {
                            return true;
                        }).catch(e => {
                            commit('purgeToken');
                            throw e;
                        });
                    } catch (e) {
                        throw e;
                    }
                })
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
            return $http.post('auth/sign-up', data).then(res => {
                const token = res.data.token;
                commit('setToken', {token: token, remember: true});
                dispatch('retrieveUser');
            });
        },
        refreshToken: ({state, commit, dispatch}) => {
            return $http.post('auth/fresh', {token: state.token}).then(res => {
                const token = res.data.token;
                commit('setToken', {token: token, remember: true});
                dispatch('retrieveUser');
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
