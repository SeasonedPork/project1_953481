<template>
  <div>Bookmark from Anime that you selected :)</div>
  <div class="scrollmenu">
    <a></a>
  </div>
  <div>Bookmark from Manga that you selected and maybe..forget :)</div>
</template>
<script>
// import EventService from "@/services/EventService";

export default {
  name: "bookMarkView",
  data() {
    return {
      Anime_array_data: [],
      manga_array_data: [],
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
    // EventService.getEvent_manga(this.mal_id)
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
