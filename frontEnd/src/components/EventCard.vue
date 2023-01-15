<template>
  <router-link to="EventDetailView, params: {id: anime.rank}">
    <div class="event-card">
      <div>random text</div>
      <h2>{{ anime.title }}</h2>
      <img :src="anime.images.jpg.image_url" alt="anime cover" />
    </div>
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
