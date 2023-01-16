<template>
  <div>Your Favorite Anime</div>
  <router-link
    :to="{ name: 'EventDetailView', params: { mal_id: anime.mal_id } }"
  >
    <img class="img" :src="anime.images.jpg.image_url" alt="anime cover" />
    <h2 style="font-size: 12px">{{ anime.title }}</h2>
  </router-link>
  <div>Recommendation</div>
</template>

<script>
import axios from "axios";

export default {
  name: "EventListView",
  props: {
    page: {
      type: Number,
      required: true,
    },
    perPage: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      Anime_data: [],
      manga_data: [],
      title: "",
      count: 0,
    };
  },
  methods: {
    getFavAnime() {
      const path = "http://127.0.0.1:5000/get_fav_anime";
      axios
        .get(path)
        .then((res) => {
          console.log(res);
          console.log("search fav anime result work");
          this.manga_data = res;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getFavManga() {
      const path = "http://127.0.0.1:5000/get_fav_manga";
      axios
        .get(path)
        .then((res) => {
          console.log(res);
          console.log("search fav manga result work");
          this.Anime_data = res;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getFavManga();
    this.getFavAnime();
  },
};
</script>
<style scoped>
.events {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.pagination {
  display: flex;
  width: 290px;
  height: 100px;
}
.pagination a {
  flex: 1;
  text-decoration: none;
  color: #2c3e50;
}
div.scrollmenu {
  background-color: #333;
  overflow: auto;
  white-space: nowrap;
}

div.scrollmenu a {
  display: inline-block;
  color: white;
  text-align: center;
  padding: 14px;
  text-decoration: none;
}
div.scrollmenu a:hover {
  background-color: #777;
}
</style>
