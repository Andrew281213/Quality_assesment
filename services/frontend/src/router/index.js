import {createRouter, createWebHistory} from 'vue-router'

import MainPage from "@/views/MainPage.vue"
import CompetenciesView from "@/views/CompetenciesView.vue";
import FacultiesView from "@/views/FacultiesView.vue";
import GroupsView from "@/views/GroupsView.vue";
import StudyPlansView from "@/views/StudyPlansView.vue";
import DisciplinesView from "@/views/DisciplinesView.vue";
import KimsView from "@/views/KimsView.vue";

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
        path: "/groups",
        name: "GroupsView",
        component: GroupsView,
        meta: {
            title: 'Группы'
        }
    },
    {
        path: "/faculties",
        name: "FacultiesView",
        component: FacultiesView,
        meta: {
            title: "Факультеты"
        }
    },
    {
        path: "/plans",
        name: "StudyPlansView",
        component: StudyPlansView,
        meta: {
            title: "Учебные планы"
        }
    },
    {
        path: "/disciplines",
        name: "DisciplinesView",
        component: DisciplinesView,
        meta: {
            title: "Дисциплины"
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
