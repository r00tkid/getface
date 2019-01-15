const Modals = {
    namespaced: true,
    state: {
        loginModal: false,
        registerModal: false,
        forgotPasswordModal: false,
    },
    mutations: {
        setLoginModal(state, value) {
            state.loginModal = !!value;
        },
        setRegisterModal(state, value) {
            state.registerModal = !!value;
        },
        setForgotPasswordModal(state, value) {
            state.forgotPasswordModal = !!value;
        }
    },
    getters: {
        login: state => {
            return state.loginModal;
        },
        register: state => {
            return state.registerModal;
        },
        forgot: state => {
            return state.forgotPasswordModal;
        }
    }
};

export default Modals;
