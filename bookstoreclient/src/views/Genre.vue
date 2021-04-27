<template>
  <div class="genre-wrapper">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">{{ genre.name }}</h2>
      </div>
    </div>
    <div class="columns is-multiline">
      <BookCards
        v-for="book in genre.books"
        v-bind:key="book.id"
        v-bind:book="book"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
import BookCards from "@/components/BookCards.vue";
export default {
  name: "Genre",
  data() {
    return {
      genre: {
        books: {},
      },
    };
  },
  components: {
    BookCards,
  },
  mounted() {
    this.getGenreDetails();
  },
  watch: {
    // eslint-disable-next-line no-unused-vars
    $route(to, from) {
      if (to.name === "Category") {
        this.getGenreDetails();
      }
    },
  },
  methods: {
    async getGenreDetails() {
      this.$store.commit("setLoading", true);

      const genere_slug = this.$route.params.genere_slug;

      await axios
        .get(`api/v1/store/genre/${genere_slug}/`)
        .then((response) => {
          this.genre = response.data;
          document.title = this.genre.name + " | BookStore";
        })
        .catch((error) => {
          console.log(error);
          toast({
            message: "Something went wrong. Please try again.",
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });
        });

      this.$store.commit("setLoading", false);
    },
  },
};
</script>