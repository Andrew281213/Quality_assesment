import {createRouter, createWebHistory} from 'vue-router'

import MainPage from "@/views/MainPage.vue"
import SpecialtiesView from "@/views/SpecialtiesView.vue"
import GroupsView from "@/views/GroupsView.vue";

const routes = [
    {
        path: '/',
        name: 'MainPage',
        component: MainPage
    },
    {
        path: '/specialties',
        name: 'SpecialtiesView',
        component: SpecialtiesView
    },
    {
        path: "/groups",
        name: "GroupsView",
        component: GroupsView
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
