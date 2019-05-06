import Vue from 'vue';
import Router from 'vue-router';

import Dashboard from '../views/layout/Dashboard';
import Landing from '../views/layout/Landing';

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
                    component: () => import('../views/tech/Empty'),
                }
            ]
        },
        {
            path: '/auth',
            component: Landing,
            children: [
                {
                    path: 'confirmation/:id/:activation',
                    name: 'auth.confirmation',
                    component: () => import('../views/auth/ConfirmRegistration'),
                },
                {
                    path: 'new-password/:id/:activation',
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
                    name: 'dashboard.main',
                    component: () => import('../views/Analitics'),
                },
                {
                    path: 'cameras',
                    name: 'dashboard.cameras',
                    component: () => import('../views/Cameras'),
                },
                {
                    path: 'client',
                    name: 'dashboard.client',
                    component: () => import('../views/Client'),
                },
                {
                    path: 'old-board',
                    name: 'dashboard.old',
                    component: () => import('../views/Home'),
                },
            ]
        },
    ],
});

/**
 * Sort of auth gate for routes
 */
router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!localStorage.token) {
            next({
                name: 'landing',
            })
        } else {
            next()
        }
    } else {
        next()
    }
});

export default router;
