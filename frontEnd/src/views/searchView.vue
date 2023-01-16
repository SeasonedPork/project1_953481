<template>
  <div>Anime searcher</div>
  <div class="search-box">
    <input
      v-model="S_input"
      placeholder="use this search bar for finding Anime"
      @keyup.enter="get_Search"
    />
    <div>{{ return_data }}</div>
    <button @click="get_Search">click to search! for ANIME!</button>
  </div>
  <div>Manga searcher</div>
  <input
    v-model="S_input_manga"
    placeholder="use this search bar for finding Manga"
    @keyup.enter="get_Search_manga"
  />
  <button @click="get_Search_manga">click to search! for MANGA!</button>
  <div>result : {{ return_data_manga }}</div>
</template>

<script>
import axios from "axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "search",
  data() {
    return {
      S_input: "",
      S_input_manga: "",
      empty: false,
      return_data: "",
      return_data_manga: "",
    };
  },
  methods: {
    // this auto-correct will be use if api is work on other PC (usual work)
    async SearchTitle() {
      const response = await fetch(
        `http://localhost:5000/title?query=${this.S_input}`
      );
      this.return_data = await response.json();
      this.S_input = "";
    },
    async SearchDescription() {
      const response = await fetch(
        `http://localhost:5000/description?query=${this.S_input}`
      );
      this.return_data = await response.json();
      console.log(this.return_data);
      this.S_input = "";
    },
    get_Search() {
      if (this.S_input === "") {
        alert("please add some input");
      } else {
        const path = "https://api.jikan.moe/v4/anime/" + this.S_input + "/full";
        axios
          .get(path)
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
    get_Search_manga() {
      if (this.S_input_manga === "") {
        alert("please add some input");
      } else {
        const path =
          "https://api.jikan.moe/v4/manga/" + this.S_input_manga + "/full";
        axios
          .get(path)
          .then((res) => {
            console.log("search result work");
            console.log(res.data);
            this.return_data_manga = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
  },
};
</script>

<style></style>
