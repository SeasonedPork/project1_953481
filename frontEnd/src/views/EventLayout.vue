<template>
  <div>
    <div>
      <div v-if="anime">
        <img :src="anime.data.images.jpg.large_image_url" />
        <h2 style="font-size: 16px">Title {{ anime.data.title }}</h2>
        <h2 style="font-size: 12px">ID : {{ anime.data.mal_id }}</h2>
        <h2 style="font-size: 11px">Story: {{ anime.data.synopsis }}</h2>
        <h2 style="font-size: 14px">
          Total Episodes: {{ anime.data.episodes }}
        </h2>
      </div>
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
