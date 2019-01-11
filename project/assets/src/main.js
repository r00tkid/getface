import '@babel/polyfill'
import Vue from 'vue'
import Vuetify from 'vuetify'
import './plugins/vuetify'
import App from './views/layout/App.vue'
import router from './control/router'
import store from './control/store'
import '@fortawesome/fontawesome-free/css/all.css'

import './control/bus'

import VueNoty from 'vuejs-noty'
import 'vuejs-noty/dist/vuejs-noty.css'

Vue.config.productionTip = false;

Vue.use(VueNoty, {
    timeout: 4000,
    progressBar: true,
    layout: 'topCenter',
    theme: 'nest'
});
Vue.use(Vuetify, {
    iconfont: 'fa4'
})
new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
