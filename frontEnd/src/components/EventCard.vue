<template>
  <router-link
    :to="{ name: 'EventDetailView', params: { mal_id: anime.mal_id } }"
  >
    <img class="img" :src="anime.images.jpg.image_url" alt="anime cover" />
    <h2 style="font-size: 12px">{{ anime.title }}</h2>
  </router-link>
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
<style>
.img:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.2);
}
</style>
