import {createRouter, createWebHistory} from 'vue-router'

import MainPage from "@/views/MainPage.vue"
import CompetenciesView from "@/views/CompetenciesView.vue";
import GroupsView from "@/views/GroupsView.vue";

const routes = [
    {
        path: '/',
        name: 'MainPage',
        component: MainPage,
        meta: {
            title: 'Кимы'
        }
    },
    {
        path: '/competencies',
        name: 'CompetenciesView',
        component: CompetenciesView,
        meta: {
            title: 'Компетенции'
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
