<template>
  <div class="search-box">
    <input
      v-model="S_input"
      placeholder="use this search bar for find your hope..."
      name="search_input"
    />
    <button @click="doGet_All">click to search!</button>
  </div>
  <div>
    <box style="font-size: 18px">
      {{ return_data }}
    </box>
  </div>
</template>

<script>
import axios from "axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "search",
  data() {
    return {
      search: {
        S_input: "",
      },
      return_data: "result show here",
    };
  },
  methods: {
    EE() {
      alert("hello");
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
    doSearch() {
      if (this.S_input === "") {
        this.emptyFields = true;
        alert("NO EMPTY NO NO!!");
      } else {
        const path = "http://127.0.0.1:5000/search";
        axios
          .post(path, {
            S_input: this.S_input,
          })
          .then((response) => {
            console.log("search is kinda work");
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

<style></style>
