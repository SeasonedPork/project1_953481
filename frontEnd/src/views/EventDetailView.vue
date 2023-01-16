<template>
  <div>
    <button @click="yoink_id">click here for book mark this!</button>
    <div v-if="anime">
      <router-view :anime="anime"></router-view>
    </div>
  </div>
</template>

<script>
import EventService from "@/services/EventService";
import axios from "axios";

export default {
  props: ["mal_id"],
  data() {
    return {
      anime: [],
    };
  },
  methods: {
    yoink_id() {
      const path = "http://127.0.0.1:5000/yoink_manga_id";
      axios
        .get(path, { params: { mal_id: this.mal_id } })
        .then((res) => {
          console.log(res);
          console.log("search result work");
          console.log(this.mal_id);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    EventService.getEvent(this.mal_id)
      .then((response) => {
        this.anime = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>
<style>
button:hover {
  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.2);
}
</style>
