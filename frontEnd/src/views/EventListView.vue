<template>
  <h1>Events For Good</h1>
  <div>
    Top anime
    <div>
      <event-card
        v-for="anime in Anime_data.data"
        :key="anime.rank"
        :anime="anime"
        style="display: inline grid"
      >
      </event-card>
    </div>
  </div>
  <div>Top manga</div>
  <div>Your favourite</div>
  <div>Recommendation</div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import EventCard from "@/components/EventCard.vue";

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
  components: { EventCard },
  data() {
    return {
      Anime_data: [],
      title: "",
    };
  },
  methods: {
    get_top() {
      const path = "http://127.0.0.1:5000/topAnime";
      axios
        .get(path)
        .then((res) => {
          console.log("top work");
          this.Anime_data = res.data;
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
  computed: {
    hasNextPage() {
      //first calculate total pages
      let totalPages = Math.ceil(this.totalEvents / 2); // 2 is events per pages

      //then check to see if the current page is less than a total pages
      return this.page < totalPages;
    },
    prevPage() {
      // First, calcalate total pages

      // Then check to see if the current page is less than the total pages.
      return this.page >= 2;
    },
    addPage() {
      return this.perPage < this.totalEvents;
    },
    Check() {
      // First, calcalate total pages

      // Then check to see if the current page is less than the total pages.
      return this.perPage >= 2;
    },
  },
  created() {
    this.get_top();
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
#page-prev {
  text-align: left;
}
#page-next {
  text-align: right;
}
</style>
