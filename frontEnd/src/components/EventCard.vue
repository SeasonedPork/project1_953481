<template>
  <router-link
    class="event-link"
    :to="{ name: 'EventDetails', params: { id: EventCard.data } }"
  >
    <div class="event-card"></div>
  </router-link>
</template>
<script>
import axios from "axios";
export default {
  name: "EventCard",

  props: {
    event: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      EventCard: [],
    };
  },
  methods: {
    get_data() {
      const path = "https://localhost:5000/EventCard";
      axios
        .get(path)
        .then((res) => {
          this.EventCard = res.data.EventCard;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.get_data();
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
