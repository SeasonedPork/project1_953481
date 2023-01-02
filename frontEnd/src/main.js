// import Vue from "vue";
// import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
// import App from "./App.vue";
// import "bootstrap/dist/css/bootstrap.css";
// import "bootstrap-vue/dist/bootstrap-vue.css";
// import router from "./router/index";
// Vue.use(BootstrapVue);
// Vue.use(IconsPlugin);
// Vue.config.productionTip = false;
// new Vue({
//   router,
//   render: (h) => h(App),
// }).$mount("#app");

import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";
import router from "@/router";

createApp(App).use(store).use(router).mount("#app");
