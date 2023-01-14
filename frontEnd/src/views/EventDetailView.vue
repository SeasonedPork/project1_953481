<template>
  <div>
    <div v-if="anime">
      <h2>{{ anime.title }}</h2>
      <img :src="anime.images.jpg.image_url" alt="anime cover" />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["rank"],
  data() {
    return {
      anime: null,
    };
  },
  methods: {
    get_top() {
      const path = "http://127.0.0.1:5000/topAnime";
      axios
        .get(path)
        .then((res) => {
          console.log("top work");
          this.top_anime = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
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
            this.return_data = response.data;
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
