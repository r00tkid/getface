import Vue from 'vue';

const bus = new Vue();
Vue.prototype.$bus = bus;

const $log = console.log;
Vue.prototype.$log = $log;

export default bus;
