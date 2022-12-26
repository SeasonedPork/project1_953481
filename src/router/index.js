import { createRouter, createWebHistory } from "vue-router";
import EventListView from "../views/EventListView.vue";
import AboutView from "../views/AboutView.vue";
import NewView from "../views/NewView.vue";

const routes = [
  {
    path: "/",
    name: "EventList",
    component: EventListView,
  },
  {
    path: "/about",
    name: "About",
    component: AboutView,
  },
  {
    path: "/new",
    name: "new",
    component: NewView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
