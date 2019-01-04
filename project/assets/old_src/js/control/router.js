import Vue from 'vue';
import Router from 'vue-router';

import Auth from '$view/layout/Auth';
import Empty from '$view/layout/Empty';

import CardLayout from '$view/tests/cards/Layout';

Vue.use(Router);

const router = new Router({
    mode: "history",
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('$view/Home'),
        },
        {
            path: '/auth',
            component: Auth,
            children: [
                {
                    path: 'sign-in',
                    name: 'auth.login',
                    component: () => import('$view/auth/SignIn'),
                },
                {
                    path: 'sign-up',
                    name: 'auth.register',
                    component: () => import('$view/auth/SignUp'),
                },
            ]
        },
        {
            path: '/test',
            component: Empty,
            children: [
                {
                    path: 'cards',
                    component: CardLayout,
                    children: [
                        {
                            path: 'add',
                            name: 'test.cards.add',
                            component: () => import('$view/tests/cards/Add'),
                        },
                        {
                            path: 'show',
                            name: 'test.cards.show',
                            component: () => import('$view/tests/cards/Show'),
                        },
                    ]
                }
            ]
        },
        {
            path: '*',
            name: 'e404',
            component: () => import('$view/errors/NotFound')
        },
    ]
});

export default router;