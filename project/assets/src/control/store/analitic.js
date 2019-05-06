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
                        id: 2.0,
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
                        id: 2.1,
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
        ],
        stat: [
            {
                name: 'Мужчины',
                checked: true,
                val: '45',
                subitems: [
                    {
                        name: 'Мужчины до 18',
                        checked: true
                    },
                    {
                        name: 'Мужчины до 18',
                        checked: true
                    },
                    {
                        name: 'Мужчины до 18',
                        checked: true
                    },
                ]
            },
            {
                name: 'Женщины',
                checked: true,
                val: '45',
                subitems: [
                    {
                        name: 'Женщины до 18',
                        checked: true
                    },
                    {
                        name: 'Женщины до 18',
                        checked: true
                    },
                    {
                        name: 'Женщины до 18',
                        checked: true
                    },
                ]
            },
            {
                name: 'Среднее время',
                checked: true,
                val: '45',
            },
            {
                name: 'Количество посещений',
                checked: true,
                val: '45',
            },
            {
                name: 'Чеки',
                checked: true,
                val: '45',
            },
            {
                name: 'Конверсия',
                checked: true,
                val: '45',
            },
        ],
        lineSeries: [
            {
                name: "Мужчины",
                data: [
                    {
                        x: "03-17-2019",
                        y: 34
                    },
                    {
                        x: "03-18-2019",
                        y: 43
                    },
                    {
                        x: "03-19-2019",
                        y: 31
                    },
                    {
                        x: "03-20-2019",
                        y: 43
                    },
                    {
                        x: "03-21-2019",
                        y: 33
                    },
                    {
                        x: "03-22-2019",
                        y: 0
                    }
                ]
            },
            {
                name: "Женщины",
                data: [
                    {
                        x: "03-17-2019",
                        y: 20
                    },
                    {
                        x: "03-18-2019",
                        y: 35
                    },
                    {
                        x: "03-19-2019",
                        y: 50
                    },
                    {
                        x: "03-20-2019",
                        y: 30
                    },
                    {
                        x: "03-21-2019",
                        y: 60
                    },
                    {
                        x: "03-22-2019",
                        y: 0
                    }
                ]
            },
            {
                name: "Ср. время",
                data: [
                    {
                        x: "03-17-2019",
                        y: 25
                    },
                    {
                        x: "03-18-2019",
                        y: 45
                    },
                    {
                        x: "03-19-2019",
                        y: 60
                    },
                    {
                        x: "03-20-2019",
                        y: 20
                    },
                    {
                        x: "03-21-2019",
                        y: 50
                    },
                    {
                        x: "03-22-2019",
                        y: 0
                    }
                ]
            }
        ]
    },
    mutations: {},
    actions: {},
    getters: {
        getAllDataTable: state => {
            return state.dataTable;
        },
        getActiveChartLine: state => {
            return state.activeChartLine;
        },
        getStat: state => {
            return state.stat;
        },
        getLineSeries: state => {
            return state.lineSeries;
        }
    }
};

export default Analitic;
