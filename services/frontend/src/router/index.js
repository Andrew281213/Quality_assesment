import {createRouter, createWebHistory} from 'vue-router'

import MainPage from "@/views/MainPage.vue"
import CompetenciesView from "@/views/CompetenciesView.vue";
import DisciplinesView from "@/views/DisciplinesView.vue";
import KimsView from "@/views/KimsView.vue";
import DirectionsView from "@/views/DirectionsView.vue";
import OpopsView from "@/views/OpopsView.vue";

const routes = [
    {
        path: '/123',
        name: 'MainPage',
        component: MainPage
    },
    {
        path: '/',
        name: 'KimsView',
        component: KimsView,
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
        path: "/disciplines",
        name: "DisciplinesView",
        component: DisciplinesView,
        meta: {
            title: "Дисциплины"
        }
    },
    {
        path: "/directions",
        name: "DirectionsView",
        component: DirectionsView,
        meta: {
            title: "Направления"
        }
    },
    {
        path: "/opops",
        name: "OpopsView",
        component: OpopsView,
        meta: {
            title: "ОПОПы"
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
