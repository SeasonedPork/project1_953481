<template>
  <div>
    <div>
      <img :src="anime.data.images.jpg.image_url" alt="anime cover" />
      <h2>Title {{ anime.data.title }}</h2>
      <div>ID : {{ anime.data.mal_id }}</div>
      <div>Story: {{ anime.data.synopsis }}</div>
      <div>Total Episodes: {{ anime.data.episodes }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["anime"],
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
