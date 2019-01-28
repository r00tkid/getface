import Vue from "vue";
import VueNoty from "vuejs-noty";
import 'vuejs-noty/dist/vuejs-noty.css';

Vue.use(VueNoty, {
    timeout: false,
    // progressBar: false,
    layout: 'topCenter',
    theme: 'nest'
});

// No default export (it's noty, man)