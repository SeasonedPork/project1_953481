// import Vue from "vue";
// import VueRouter from "vue-router";
// import Frontview from "../views/AboutView.vue";
// import HelloWorld from "@/components/HelloWorld.vue";
// Vue.use(VueRouter);
// export default new VueRouter({
//   mode: "history",
//   routes: [
//     {
//       path: "/",
//       name: "Frontview",
//       component: Frontview,
//     },
//     {
//       path: "/dummy",
//       name: "HelloWorld",
//       component: HelloWorld,
//     },
//   ],
// });

import { createRouter, createWebHistory } from "vue-router";
import EventListView from "../views/EventListView.vue";
import AboutView from "../views/AboutView.vue";
import SearchView from "@/views/searchView.vue";
// import Eventcard from "@/components/EventCard.vue";
import EventDetailView from "@/views/EventDetailView.vue";
// import EventDetails from '../views/EventDetailViews.vue'

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
    path: "/EventDetailView",
    name: "EventDetailView",
    component: EventDetailView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
