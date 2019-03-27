import '@babel/polyfill'
import Vue from 'vue'
import './control/axios'
import './control/bus'
import './plugins/notify'
import './plugins/vuetify'
import Vuetify from 'vuetify'
import App from './views/layout/App.vue'
import router from './control/router'
import store from './control/store'
import '@fortawesome/fontawesome-free/css/all.css'
import i18n from './control/i18n'
import VueApexCharts from 'vue-apexcharts'
import './plugins/log';

Vue.use(VueApexCharts);
Vue.component('apexchart', VueApexCharts);

Vue.config.productionTip = false;

const settings = require('./../package.json');

Vue.prototype.versions = {
    'front': settings["version"],
    'back': settings["back-version"],
    'build': settings["project-build"],
};

window.collections = require('./other/object').default;

Vue.use(Vuetify, {
    iconfont: 'fa4'
});

window.get_face = new Vue({
    router,
    store,
    i18n,
    render: h => h(App)
}).$mount('#app');
