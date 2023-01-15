import { createRouter, createWebHistory } from "vue-router";
import EventListView from "../views/EventListView.vue";
import AboutView from "../views/AboutView.vue";
import SearchView from "@/views/searchView.vue";
import EventDetailView from "@/views/EventDetailView.vue";
import EventLayoutView from "@/views/EventLayout.vue";

const routes = [
  {
    path: "/",
    name: "EventList",
    component: EventListView,
    props: (route) => ({
      page: parseInt(route.query.page) || 1,
      perPage: parseInt(route.query.perPage) || 1,
    }),
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
  },
  {
    path: "/search",
    name: "search",
    component: SearchView,
  },
  {
    path: "/EventDetailView/:mal_id",
    name: "EventDetailView",
    props: true,
    component: EventDetailView,
    children: [
      {
        path: "",
        name: "EventLayoutView",
        component: EventLayoutView,
        props: true,
      },
    ],
  },
  // {
  //   path: "/EventDetailView",
  //   name: "EventDetailView",
  //   component: EventDetailView,
  // },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
