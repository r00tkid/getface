const Cards = {
    namespaced: true,
    state: {},
    mutations: {
        setCard: (state, payload_object) => {
            state[payload_object.uid] = payload_object;
        }
    },
    getters: {
        getCard: state => uuid => {
            return state[uuid];
        },
        getCards: state => [...state].filter((obj, index) => {
            if (obj.checked) {
                return obj;
            }

            return false;
        })
    },
};

export default Cards;