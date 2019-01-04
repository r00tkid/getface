const base_url = "/api/v1";

const Api = {
    namespaced: true,
    state: {
        user: {
            login: `${base_url}/auth/sign-in`,
            register: `${base_url}/auth/sign-up`,
            crud: `${base_url}/user/`,
        }
    },
    mutations: {},
    getters: {
        url: state => name => {
            try {
                let result = state;
                let parts = name.split('.');
                for (let i = 0; i < parts.length; i++) result = result[parts[i]];
                return result;
            } catch (e) {
                return null;
            }
        },
    },
};

export default Api;