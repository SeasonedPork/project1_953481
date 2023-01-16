<template>
  <div>Your Favorite Anime</div>
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
  <div>Your Favorite manga</div>
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
  <div>Your favourite</div>
  <div>Recommendation</div>
</template>

<script>
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
      manga_data: [],
      title: "",
      count: 0,
    };
  },
  methods: {},
  created() {},
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
