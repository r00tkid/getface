const Analitic = {
    state: {
        dataTable: [
            {
                name: "Камера 1",
                id: 0,
                selected: true,
                amount: "500 чел (15%)",
                mood: "Плохое-15%",
                male: "250 чел (50%)",
                female: "250 чел (50%)",
                averageTime: "150ч:30м",
                heavyCars: "250 (50%)",
                lightCars: "250 (50%)"
            },
            {
                name: "Камера 2",
                id: 1,
                selected: true,
                amount: "500 чел (15%)",
                mood: "Плохое-15%",
                male: "250 чел (50%)",
                female: "250 чел (50%)",
                averageTime: "150ч:30м",
                heavyCars: "250 (50%)",
                lightCars: "250 (50%)"
            },
            {
                name: "Зона 1",
                id: 2,
                selected: false,
                amount: "500 чел (15%)",
                mood: "Плохое-15%",
                male: "250 чел (50%)",
                female: "250 чел (50%)",
                averageTime: "150ч:30м",
                heavyCars: "250 (50%)",
                lightCars: "250 (50%)",
                items: [
                    {
                        name: "Камера 5",
                        selected: false,
                        amount: "500 чел (15%)",
                        mood: "Плохое-15%",
                        male: "250 чел (50%)",
                        female: "250 чел (50%)",
                        averageTime: "150ч:30м",
                        heavyCars: "250 (50%)",
                        lightCars: "250 (50%)"
                    },
                    {
                        name: "Камера 6",
                        selected: false,
                        amount: "500 чел (15%)",
                        mood: "Плохое-15%",
                        male: "250 чел (50%)",
                        female: "250 чел (50%)",
                        averageTime: "150ч:30м",
                        heavyCars: "250 (50%)",
                        lightCars: "250 (50%)"
                    }
                ]
            }
        ]
    },
    mutations: {

    },
    actions: {

    },
    getters: {
        getAllDataTable: state => {
            return state.dataTable;
        },
    }
};

export default Analitic;
