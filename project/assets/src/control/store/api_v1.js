const base = '/api/v1/';

function isVariableAFunction(functionToCheck) {
    return functionToCheck && {}.toString.call(functionToCheck) === '[object Function]';
}

const V1 = {
    namespaced: true,
    state: {
        url: {
            auth: (resolve) => {
                let route = {
                    login: 'sign-in',
                    register: 'sign-up',
                    refresh: 'refresh',
                    user: 'me',
                    resend: 'resend',
                    confirmation: 'confirm',

                    password_restore: 'lost',
                    password_reset: 'reset',
                }[resolve];

                return `${base}auth/${route}`;
            },
            payment: (resolve) => {
                let route = {
                    rate: (resolve) => {
                        let route = {
                            available: 'available',
                            buy: 'buy',
                        }[resolve];

                        return `${base}payment/rate/${route}`;
                    },
                }[resolve];

                return isVariableAFunction(route) ? route : `${base}payment/${route}`;
            },
        },
    },
    mutations: {},
    getters: {
        uri: state => name => {
            let named_route = name.split('.');
            let result = state.url[named_route[0]];

            for (let i = 1; i < named_route.length; i++) {
                result = result(named_route[i]);
            }

            return result;
        },
    }
};

export default V1;