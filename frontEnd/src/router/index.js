import { createRouter, createWebHistory } from "vue-router";
import EventListView from "../views/EventListView.vue";
import RegisterView from "../views/RegisterView.vue";
import SearchView from "@/views/searchView.vue";
import EventDetailView from "@/views/EventDetailView.vue";
import EventLayoutView from "@/views/EventLayout.vue";
import EventDetailViewManga from "@/views/EventDetailViewManga.vue";
import EventLayoutManga from "@/views/EventLayoutManga.vue";
import Bookmark from "@/views/bookmark.vue";
import yourFavView from "@/views/YourFavView.vue";

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
    path: "/RegisterView",
    name: "RegisterView",
    component: RegisterView,
  },
  {
    path: "/search",
    name: "search",
    component: SearchView,
  },
  {
    path: "/bookmark",
    name: "bookMarkView",
    component: Bookmark,
    props: (route) => ({
      page: parseInt(route.query.page) || 1,
      perPage: parseInt(route.query.perPage) || 1,
    }),
  },
  {
    path: "/yourFav",
    name: "yourFavView",
    component: yourFavView,
    props: (route) => ({
      page: parseInt(route.query.page) || 1,
      perPage: parseInt(route.query.perPage) || 1,
    }),
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
  {
    path: "/EventDetailViewManga/:mal_id",
    name: "EventDetailViewManga",
    component: EventDetailViewManga,
    children: [
      {
        path: "",
        name: "EventLayoutViewManga",
        component: EventLayoutManga,
        props: true,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
