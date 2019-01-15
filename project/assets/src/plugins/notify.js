import Vue from "vue";
import VueNoty from "vuejs-noty";
import 'vuejs-noty/dist/vuejs-noty.css';

Vue.use(VueNoty, {
    timeout: 4000,
    progressBar: true,
    layout: 'topCenter',
    theme: 'nest'
});

// No default export (it's noty, man)