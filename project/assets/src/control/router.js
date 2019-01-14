import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
import Profile from '../views/Profile'
import Calendar from '../views/Calendar'
import Auth from '../views/Auth'
import Login from '../components/modals/LoginModal'
import Register from '../components/modals/RegisterModal'


import Dashboard from '../views/layout/Dashboard'

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            component: Auth,
            children: [
                {
                    path: '/login',
                    name: 'login',
                    component: Login
                },
                {
                    path: '/register',
                    name: 'register',
                    component: Register
                },
            ]
        },
        {
            path: '/dashboard',
            component: Dashboard,
            meta: { requiresAuth: true },
            children: [
                {
                    path: '',
                    name: 'home',
                    component: Home
                },
                {
                    path: '/profile',
                    name: 'profile',
                    component: Profile
                },
                {
                    path: '/calendar',
                    name: 'calendar',
                    component: Calendar
                }
            ]
        },
    ],
});
