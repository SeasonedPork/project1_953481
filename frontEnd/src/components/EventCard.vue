<template>
  <div class="event-card">
    <router-link
      :to="{ name: 'EventDetailView', params: { mal_id: anime.mal_id } }"
    >
      <h2>{{ anime.title }}</h2>
      <div>{{ anime.mal_id }}</div>
      <img :src="anime.images.jpg.image_url" alt="anime cover" />
    </router-link>
  </div>
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
.event-card {
  padding: 20px;
  width: 250px;
  cursor: pointer;
  border: 1px solid #39495c;
  margin-bottom: 18px;
}

.event-card:hover {
  transform: scale(1.01);
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2);
}
.event-link {
  color: #2c3e50;
  text-decoration: none;
}
</style>
