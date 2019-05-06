const Home = {
    state: {
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
        ],
        stat: [
            {
                name: "Нарушений",
                checked: true,
                val: "45"
              },
              {
                name: "Опозданий",
                checked: true,
                val: "45"
              },
              {
                name: "Ушел раньше",
                checked: true,
                val: "45"
              },
              {
                name: "Разница часов",
                checked: true,
                val: "45"
              },
              {
                name: "Факт часов",
                checked: true,
                val: "45"
              },
              {
                name: "План часов",
                checked: true,
                val: "45"
              },
              {
                name: "Настроение",
                checked: true,
                val: "45"
              },
              {
                name: "Усталость",
                checked: true,
                val: "45"
              }
        ]
    },
    mutations: {
       
    },
    actions: {

    },
    getters: {
        getHomeDataTable: state => {
            return state.dataTable;
        },
        getHomeStat: state => {
            return state.stat;
        },
        getSeries: state =>{
            return state.lineSeries;
        }
    }
};

export default Home;
