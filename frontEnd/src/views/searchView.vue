<template>
  <div>Anime searcher</div>
  <div class="search-box">
    <input
      v-model="S_input"
      placeholder="use this search bar for finding Anime"
      @keyup.enter="get_Search"
    />
    <button @click="get_Search">click to search! for ANIME!</button>
  </div>
  <div>Manga searcher</div>
  <input
    v-model="S_input_manga"
    placeholder="use this search bar for finding Manga"
    @keyup.enter="get_Search"
  />
  <button @click="get_Search">click to search! for MANGA!</button>
  <div>result : {{ return_data }}</div>
</template>

<script>
import axios from "axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "search",
  data() {
    return {
      S_input: "",
      empty: false,
      return_data: "",
    };
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
  },
};
</script>

<style></style>
