import '@babel/polyfill'
import Vue from 'vue'
import Vuetify from 'vuetify'
import './plugins/vuetify'
import App from './views/layout/App.vue'
import router from './control/router'
import store from './control/store'
import '@fortawesome/fontawesome-free/css/all.css'

import './control/axios'
import './control/bus'
import './plugins/notify'

Vue.config.productionTip = false;

Vue.use(Vuetify, {
    iconfont: 'fa4'
});

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
