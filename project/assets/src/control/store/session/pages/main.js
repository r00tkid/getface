const Main = {
    namespaced: true,
    state: {
        showAnalytics: true,
    },
    mutations: {
        swapAnalytics: state => {
            state.showAnalytics = !state.showAnalytics;
        }
    },
};

export default Main;