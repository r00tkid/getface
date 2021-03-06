const Auth = {
    namespaced: true,
    state: {
        last_fetched_rates: null,
        current_company: null,
        authenticated: false,
        has_rights: false,
        companies: {},
        token: '',
        user: {},
    },
    mutations: {
        setAuth: (state, payload) => {
            state.authenticated = payload;
        },
        setUser: (state, payload) => {
            state.authenticated = !!payload.user;
            state.user = payload.user;
            state.companies = payload.companies;
        },
        setToken: (state, payload) => {
            localStorage.setItem('token', payload.token);
            state.token = payload.token;
        },
        setCompanies: (state, payload) => {
            localStorage.setItem('companies', JSON.stringify(payload.companies));
            state.companies = payload.companies;
        },
        purgeToken: state => {
            console.log("Looking for exit");

            localStorage.removeItem('token');
            state.token = '';
        },
        purgeUser: state => {
            state.user = {};
        },
        purgeAuth: state => {
            state.authenticated = false;
        },
        setRights: (state, payload) => {
            state.has_rights = payload;
        },
        setCurrentCompany: (state, company) => {
            state.current_company = company;
        },
        setFetchedRates: (state, rates) => {
            state.last_fetched_rates = rates;
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
        companies: state => {
            try {
                return state.companies || JSON.parse(localStorage.getItem('get-face-user-companies'));
            } catch (e) {
                return null;
            }
        },
        isAuth: state => state.authenticated,
        token: state => state.token,
        hasRights: state => state.has_rights,
    }
};

export default Auth;
