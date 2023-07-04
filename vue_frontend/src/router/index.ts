import { RouteRecordRaw, createRouter, createWebHistory } from "vue-router"

const routes: RouteRecordRaw[] = [
    {
        path: "/",
        name: "home",
        component: () => import("@/App.vue"),
    },
    {
        path: "/tasks/:id",
        name: "tasks-details",
        component: () => import("@/components/TaskDetail.vue"),
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;