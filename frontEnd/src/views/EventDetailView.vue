<template>
  <div>
    <div v-if="anime || mal_id">
      <div id="nav">
        <router-view :anime="anime"></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import EventService from "@/services/EventService";

export default {
  props: ["mal_id"],
  data() {
    return {
      anime: null,
    };
  },
  created() {
    EventService.getEvent(this.mal_id)
      .then((response) => {
        this.anime = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>
