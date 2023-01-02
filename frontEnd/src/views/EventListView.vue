<template>
  <h1>Events For Good</h1>
  <div class="events">
    <EventCard
      v-for="event in events"
      :key="event.id"
      :event="event"
    ></EventCard>
    <div class="pagination">
      <router-link
        id="page-prev"
        :to="{ name: 'EventList', query: { page: page - 1 } }"
        rel="prev"
        v-if="page != 1"
        >Prev Page</router-link
      >
      <router-link
        id="page-next"
        :to="{ name: 'EventList', query: { page: page + 1 } }"
        rel="next"
        v-if="prevPage"
        >Next Page</router-link
      >
      <router-link
        id="page-size-minus"
        :to="{ name: 'EventList', query: { size: size - 1 } }"
        rel="next"
        v-if="addPage"
        >Decrese SIZE</router-link
      >
      <router-link
        id="page-size-plus"
        :to="{ name: 'EventList', query: { size: size + 1 } }"
        rel="next"
        v-if="check"
        >Increase SIZE</router-link
      >
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import EventCard from "../components/EventCard.vue";
import EventService from "../services/EventService.js";
import { watchEffect } from "@vue/runtime-core";

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
  components: {
    EventCard,
  },
  data() {
    return {
      events: null,
      totalEvents: 0, // add thiis for store totalevent
      size: 2,
    };
  },
  created() {
    watchEffect(() => {
      EventService.getEvents(this.perPage, this.page)
        .then((response) => {
          this.events = response.data;
          this.totalEvents = response.headers["x-total-count"];
        })
        .catch((error) => {
          console.log(error);
        });
    });
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
