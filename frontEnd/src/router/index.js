import Vue from "vue";
import VueRouter from "vue-router";
import Frontview from "../views/AboutView.vue";
import HomeView from "../views/HomeView.vue";

Vue.use(VueRouter);
export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Frontview",
      component: Frontview,
    },
    {
      path: "/",
      name: "HelloWorld",
      component: HomeView,
    },
  ],
});
