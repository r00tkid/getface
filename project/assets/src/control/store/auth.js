const Auth = {
    namespaced: true,
    state: {
        authenticated: false,
        user: {},
        companies: {},
        token: '',
    },
    mutations: {
        setAuth: (state, payload) => {
            state.authenticated = payload;
        },
        setUser: (state, payload) => {
            state.user = payload.user;
            state.companies = payload.companies;
        },
        setToken: (state, payload) => {
            state.token = payload.token;
            localStorage.setItem('token', payload.token);
        },
        purgeToken: state => {
            state.token = '';
            localStorage.removeItem('token');
        },
        purgeUser: state => {
            state.user = {};
        },
        purgeAuth: state => {
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
        token: state => state.token,
    }
};

export default Auth;
