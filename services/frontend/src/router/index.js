import {createRouter, createWebHistory} from 'vue-router'

import MainPage from "@/views/MainPage.vue"
import CompetenciesView from "@/views/CompetenciesView.vue";
import DisciplinesView from "@/views/DisciplinesView.vue";
import KimsView from "@/views/KimsView.vue";
import DirectionsView from "@/views/DirectionsView.vue";
import OpopsView from "@/views/OpopsView.vue";
import DirectionView from "@/views/DirectionView.vue";
import DirectionCreateView from "@/views/DirectionCreateView.vue";
import OpopCreateView from "@/views/OpopCreateView.vue";
import OpopView from "@/views/OpopView.vue";
import DisciplineView from "@/views/DisciplineView.vue";
import DisciplineCreateView from "@/views/DisciplineCreateView.vue"

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
        path: "/disciplines/:discipline_id",
        name: "DisciplineView",
        component: DisciplineView,
        props: true
    },
    {
        path: "/disciplines/create",
        name: "DisciplineCreateView",
        component: DisciplineCreateView,
        meta: {
            title: "Создание дисциплины"
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
        path: "/directions/:direction_id",
        name: "DirectionView",
        component: DirectionView,
        props: true
    },
    {
        path: "/directions/create",
        name: "DirectionCreateView",
        component: DirectionCreateView,
        meta: {
            title: "Создание направления"
        }
    },
    {
        path: "/opops",
        name: "OpopsView",
        component: OpopsView,
        meta: {
            title: "ОПОПы"
        }
    },
    {
        path: "/opops/:opop_id",
        name: "OpopView",
        component: OpopView,
        props: true
    },
    {
        path: "/opops/create",
        name: "OpopCreateView",
        component: OpopCreateView,
        meta: {
            title: "Создание ОПОПа"
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
