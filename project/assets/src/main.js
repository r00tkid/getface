import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import App from './views/layout/App.vue'
import router from './control/router'
import store from './control/store'

import VueNoty from 'vuejs-noty'
import 'vuejs-noty/dist/vuejs-noty.css'

Vue.config.productionTip = false;
Vue.prototype.$bus = new Vue;

Vue.use(VueNoty, {
    timeout: 4000,
    progressBar: true,
    layout: 'topCenter',
    theme: 'nest'
});

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
