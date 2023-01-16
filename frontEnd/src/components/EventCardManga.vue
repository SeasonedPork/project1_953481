<template>
  <router-link
    :to="{
      name: 'EventDetailViewManga',
      params: { mal_id: manga.mal_id },
    }"
  >
    <img class="img" :src="manga.images.jpg.image_url" alt="anime cover" />
    <h2 style="font-size: 12px">{{ manga.title }}</h2>
  </router-link>
</template>
<script>
export default {
  name: "EventCardManga",
  props: {
    manga: {
      type: Object,
      required: true,
    },
  },
  methods: {
    sometext() {
      console.log("eventcard manga run");
    },
  },
  created() {
    this.sometext();
  },
};
</script>
<style>
.img:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.2);
}
</style>
