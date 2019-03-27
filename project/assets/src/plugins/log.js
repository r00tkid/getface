import Vue from "vue";

Vue.prototype.$log = 'development' === process.env.NODE_ENV ? console.log.bind(console) : (message, ...options) => {};