<template>
  <div class="g">Your Favorite Anime</div>
  <button @click="DeleteFavAnime">
    click here to removed it from Favourite
  </button>
  <div class="scrollmenu">
    <a>
      <event-card
        v-for="anime in get_data"
        :key="anime.data.mal_id"
        :anime="anime.data"
      >
      </event-card>
    </a>
    <div style="text-underline-color: #39b982">{{ Anime_data }}</div>
  </div>
</template>

<script>
import EventCard from "@/components/EventCard.vue";
import axios from "axios";
import EventService from "@/services/EventService";

export default {
  name: "yourFav",
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
  components: { EventCard },
  data() {
    return {
      Anime_data: [8],
      get_data: [],
      title: "",
      count: 0,
    };
  },
  methods: {
    DeleteFavAnime() {
      const path = "http://127.0.0.1:5000/Delete_fav_anime";
      axios
        .get(path, { params: { mal_id: this.mal_id } })
        .then((res) => {
          console.log(res);
          console.log("search fav anime result work");
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getBookmarkAnime() {
      const path = "http://127.0.0.1:5000/get_bookmark_anime";
      axios
        .get(path)
        .then((res) => {
          console.log(res);
          console.log("search fav anime result work");
          this.Anime_data = res.data;
          for (let i = 0; i < this.Anime_data.length; i++) {
            console.log("this shit work");
            EventService.getEvent(this.Anime_data[i])
              .then((response) => {
                this.get_data.push(response.data);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getBookmarkAnime();
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
.g {
  font-size: 24px;
  font-family: "Book Antiqua", serif;
  font-weight: bolder;
}
</style>
