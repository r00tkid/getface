const Tech = {
    namespaced: true,
    state: {
        regex: {
            email: /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
        }
    },
    mutations: {},
    getters: {
        emailValidate: state => email => {
            return state.regex.email.test(email);
        },
    },
};

export default Tech;