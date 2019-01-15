import Vue from 'vue'
import Router from 'vue-router'

import Auth from '../views/Auth' // Layout?
import Dashboard from '../views/layout/Dashboard'

Vue.use(Router);

const router = new Router({
    mode: 'history',
    // base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            component: Auth,
            children: [
                {
                    path: '/login',
                    name: 'login',
                    component: () => import('../components/modals/LoginModal')
                },
                {
                    path: '/register',
                    name: 'register',
                    component: () => import('../components/modals/RegisterModal')
                },
            ]
        },
        {
            path: '/dashboard',
            component: Dashboard,
            meta: {requiresAuth: true},
            children: [
                {
                    path: '',
                    name: 'home',
                    component: () => import('../views/Home')
                },
                {
                    path: '/profile',
                    name: 'profile',
                    component: () => import('../views/Profile')
                },
                {
                    path: '/calendar',
                    name: 'calendar',
                    component: () => import('../views/Calendar')
                }
            ]
        },
        {
            path: '/ghost',
            name: 'ghost',
            component: () => import('../views/Ghost'),
        },
    ],
});

export default router;

/**
 * Sort of auth gate for routes
 */
router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {

        if (localStorage.getItem('token') == null) {
            next({
                to: 'login',
                params: {nextUrl: to.fullPath}
            })
        } else {
            next()
        }
    } else {
        next()
    }
});
