import {createRouter, createWebHistory} from 'vue-router'

import MainPage from "@/views/MainPage.vue"
import SpecialtiesView from "@/views/SpecialtiesView.vue"
import GroupsView from "@/views/GroupsView.vue";

const routes = [
    {
        path: '/',
        name: 'MainPage',
        component: MainPage,
        meta: {
            title: 'Главная страница'
        }
    },
    {
        path: '/specialties',
        name: 'SpecialtiesView',
        component: SpecialtiesView,
        meta: {
            title: 'Специальности'
        }
    },
    {
        path: "/groups",
        name: "GroupsView",
        component: GroupsView,
        meta: {
            title: 'Группы'
        }
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    if (to.meta.title) {
        document.title = to.meta.title
    }
    next()
})

export default router
