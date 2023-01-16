<template>
  <div
    style="
      font-size: 24px;
      font-family: 'Book Antiqua', serif;
      font-weight: bolder;
    "
  >
    Top Anime
  </div>
  <div class="scrollmenu">
    <a>
      <event-card
        v-for="anime in Anime_data.data"
        :key="anime.mal_id"
        :anime="anime"
      >
      </event-card>
    </a>
  </div>
  <div
    style="
      font-size: 24px;
      font-family: 'Book Antiqua', serif;
      font-weight: bolder;
    "
  >
    Top manga
  </div>
  <div class="scrollmenu">
    <a>
      <event-card-manga
        v-for="manga in manga_data.data"
        :key="manga.mal_id"
        :manga="manga"
      >
      </event-card-manga>
    </a>
  </div>
  <div
    style="
      font-size: 24px;
      font-family: 'Book Antiqua', serif;
      font-weight: bolder;
    "
  >
    Your favourite
  </div>
  <div
    style="
      font-size: 24px;
      font-family: 'Book Antiqua', serif;
      font-weight: bolder;
    "
  >
    Recommendation?
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import EventCard from "@/components/EventCard.vue";
import EventCardManga from "@/components/EventCardManga.vue";

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
  components: { EventCardManga, EventCard },
  data() {
    return {
      Anime_data: [],
      Anime_top_data: [],
      manga_data: [],
      manga_top_data: [],
      title: "",
      count: 0,
    };
  },
  methods: {
    doGet_All_M() {
      if (this.S_input === "") {
        this.emptyFields = true;
        alert("NO EMPTY NO NO!!");
      } else {
        const path = "http://127.0.0.1:5000/get_All_manga";
        axios
          .get(path)
          .then((response) => {
            this.manga_data = response.data;
            console.log("GetALL is kinda work");
            return response;
          })
          .catch((err) => {
            console.log(err);
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
            console.log("GetALL is kinda work");
            return response;
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
  created() {
    this.doGet_All();
    this.doGet_All_M();
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
  overflow-y: scroll;
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
