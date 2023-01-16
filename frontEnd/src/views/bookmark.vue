<template>
  <router-link
    :to="{ name: 'EventDetailView', params: { mal_id: anime.mal_id } }"
  >
    <img class="img" :src="anime.images.jpg.image_url" alt="anime cover" />
    <h2 style="font-size: 12px">{{ anime.title }}</h2>
  </router-link>
</template>
<script>
import axios from "axios";

export default {
  name: "EventCard",
  props: {
    anime: {
      type: Object,
      required: true,
    },
  },
  methods: {
    get_Search() {
      if (this.S_input === "") {
        alert("please add some input");
      } else {
        const path = "http://127.0.0.1:5000/search";
        axios
          .get(path, { params: { S_input: this.S_input } })
          .then((res) => {
            console.log("search result work");
            console.log(res.data);
            this.return_data = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    doGet_All() {
      if (this.S_input === "") {
        this.emptyFields = true;
        alert("NO EMPTY NO NO!!");
      } else {
        const path = "http://127.0.0.1:5000/get_All";
        axios
          .get(path)
          .then((response) => {
            this.Anime_data = response.data;
            this.count = Object.keys(response.data).length;
            console.log("GetALL is kinda work");
            return response;
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
};
</script>
<style>
.img:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.2);
}
</style>
