const Auth = {
    namespaced: true,
    state: {
        authenticated: false,
        user: {},
        companies: {},
        token: '',
        has_rights: false,
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
        setRights: (state, payload) => {
            state.has_rights = payload;
        }
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
        hasRights: state => state.has_rights,
    }
};

export default Auth;
