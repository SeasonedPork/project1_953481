import axios from "axios";

const apiClient = axios.create({
  baseURL: "https://api.jikan.moe/v4/",
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

export default {
  getEvent(id) {
    return apiClient.get("anime/" + id + "/full");
  },
  yoink_id(id) {
    return id;
  },
  getEvent_manga(id) {
    return apiClient.get("manga/" + id + "/full");
  },
};
