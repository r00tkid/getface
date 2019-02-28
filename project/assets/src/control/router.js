import Vue from 'vue'
import Router from 'vue-router'

import Dashboard from '../views/layout/Dashboard'
import Landing from '../views/layout/Landing'

Vue.use(Router);

const router = new Router({
    mode: 'history',
    //base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            component: Landing,
            children: [
                {
                    path: '',
                    name: 'landing',
                    component: () => import('../views/tech/Empty')
                }
            ]
        },
        {
            path: '/auth',
            component: Landing,
            children: [
                {
                    path: '/confirmation/:id/:activation',
                    name: 'auth.confirmation',
                    component: () => import('../views/auth/ConfirmRegistration'),
                },
                {
                    path: '/new-password/:id/:activation',
                    name: 'auth.password',
                    component: () => import('../views/auth/NewPassword'),
                }
            ]
        },
        {
            path: '/dashboard',
            component: Dashboard,
            meta: {requiresAuth: true},
            children: [
                {
                    path: 'main',
                    name: 'dashboard',
                    component: () => import('../views/Home')
                },
                {
                    path: 'profile',
                    name: 'profile',
                    component: () => import('../views/Profile')
                },
                {
                    path: 'calendar',
                    name: 'calendar',
                    component: () => import('../views/Calendar')
                },
                {
                    path: 'employee',
                    name: 'employee',
                    component: () => import('../views/Employee')
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


/**
 * Sort of auth gate for routes
 */
router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!localStorage.token && !sessionStorage.token) {
            next({
                path: '/',
            })
        } else {
            next()
        }
    } else {
        next()
    }
});

export default router;
