import '@babel/polyfill'
import Vue from 'vue'
import Vuetify from 'vuetify'
import './plugins/vuetify'
import App from './views/layout/App.vue'
import router from './control/router'
import store from './control/store'
import '@fortawesome/fontawesome-free/css/all.css'

window._ = require('lodash');


import './control/axios'
import './control/bus'
import './plugins/notify'

Vue.config.productionTip = false;

const settings = require('./../package.json');
Vue.prototype.versions = {
    'front': settings["version"],
    'back': settings["back-version"],
    'build': settings["project-build"],
};

Vue.use(Vuetify, {
    iconfont: 'fa4'
});

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
