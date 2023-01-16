<template>
  <div>Your favourite Anime</div>
  <div class="scrollmenu">
    <a></a>
  </div>
  <div>Your favourite Manga</div>
</template>
<script>
// import EventService from "@/services/EventService";

export default {
  name: "YourFavView",
  data() {
    return {
      Anime_data: [],
      Anime_top_data: [],
      manga_data: [],
      manga_top_data: [],
      input: [],
      count: 0,
    };
  },
  created() {
    // EventService.getEvent(this.mal_id)
    //   .then((response) => {
    //     this.anime = response.data;
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });
  },
};
</script>
<style>
.img:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.2);
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
