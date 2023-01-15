<template>
  <b-card>
    <router-link
      :to="{ name: 'EventDetailView', params: { mal_id: anime.mal_id } }"
      style="text-align: center"
    >
      <h2 style="font-size: 14px">{{ anime.title }}</h2>
      <img class="img" :src="anime.images.jpg.image_url" alt="anime cover" />
    </router-link>
  </b-card>
</template>
<script>
export default {
  name: "EventCard",
  props: {
    anime: {
      type: Object,
      required: true,
    },
  },
};
</script>
<style scoped>
.img:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.2);
}
.event-link {
  color: #2c3e50;
  text-decoration: none;
}
</style>
