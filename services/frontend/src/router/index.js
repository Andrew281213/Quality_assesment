import {createRouter, createWebHistory} from 'vue-router'

import MainPage from "@/views/MainPage.vue"
import CompetenciesView from "@/views/listViews/CompetenciesView.vue";
import DisciplinesView from "@/views/listViews/DisciplinesView.vue";
import KimsView from "@/views/listViews/KimsView.vue";
import DirectionsView from "@/views/listViews/DirectionsView.vue";
import OpopsView from "@/views/listViews/OpopsView.vue";
import DirectionView from "@/views/oneViews/DirectionView.vue";
import DirectionCreateView from "@/views/createViews/DirectionCreateView.vue";
import OpopCreateView from "@/views/createViews/OpopCreateView.vue";
import OpopView from "@/views/oneViews/OpopView.vue";
import DisciplineView from "@/views/oneViews/DisciplineView.vue";
import DisciplineCreateView from "@/views/createViews/DisciplineCreateView.vue"
import CompetenceCreateView from "@/views/createViews/CompetenceCreateView.vue";
import CompetenceView from "@/views/oneViews/CompetenceView.vue";

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
        path: "/competencies/:competence_id",
        name: "CompetenceView",
        component: CompetenceView,
        props: true
    },
    {
        path: "/competencies/create",
        name: "CompetenceCreateView",
        component: CompetenceCreateView,
        meta: {
            title: "Создание компетенции"
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
