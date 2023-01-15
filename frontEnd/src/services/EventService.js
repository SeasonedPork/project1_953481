import axios from "axios";

const apiClient = axios.create({
  baseURL: "https://api.jikan.moe/v4/anime",
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

export default {
  getEvent(id) {
    return apiClient.get("/" + id + "/full");
  },
};
