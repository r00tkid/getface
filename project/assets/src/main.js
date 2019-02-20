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

window._ = require('lodash');
Vue.config.productionTip = false;

const settings = require('./../package.json');

Vue.prototype.versions = {
    'front': settings["version"],
    'back': settings["back-version"],
    'build': settings["project-build"],
};

Vue.prototype.$log = console.log;

Vue.use(Vuetify, {
    iconfont: 'fa4'
});

window.get_face = new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
