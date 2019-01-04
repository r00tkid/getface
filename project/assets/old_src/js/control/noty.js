import VueNoty from 'vuejs-noty';
import Vue from 'vue';

import 'vuejs-noty/dist/vuejs-noty.css';

Vue.use(VueNoty, {
    timeout: 3000,
    layout: 'bottomCenter',
    theme: 'metroui',
});