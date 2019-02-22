const Auth = {
    namespaced: true,
    state: {
        authenticated: false,
        user: {},
        companies: {},
        token: '',
    },
    mutations: {
        setAuth(state, value) {
            state.authenticated = value;
        },
        setUser(state, value) {
            state.user = value.user;
            state.companies = value.companies;
        },
        setToken(state, value) {
            state.token = value.token;
            value.remember ? localStorage.setItem('token', value.token) : sessionStorage.setItem('token', value.token);
        },
        purgeToken(state) {
            state.token = '';
            localStorage.removeItem('token');
            sessionStorage.removeItem('token');
        },
        purgeUser(state) {
            state.user = {};
        },
        purgeAuth(state) {
            state.authenticated = false;
        },
    },
    actions: {
        logout: ({commit}) => {
            return new Promise((resolve) => {
                commit('purgeToken');
                commit('purgeUser');
                commit('purgeAuth');
                resolve(true);
            });
        },
    },
    getters: {
        user: state => state.user,
        companies: state => state.companies,
        isAuth: state => state.authenticated,
    }
};

export default Auth;
