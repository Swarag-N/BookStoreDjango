<template>
  <div class="search-wrapper">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Search</h1>

        <h2 class="is-size-5 has-text-grey">Search term: "{{ query }}"</h2>
      </div>

      <BookCards
        v-for="book in books"
        v-bind:key="book.id"
        v-bind:book="book"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import BookCards from "@/components/BookCards.vue";

export default {
  name: "Search",
  data() {
    return {
      books: {},
      query: "",
    };
  },
  components: {
    BookCards,
  },
  mounted() {
    // document.title = 'Search | Djackets'
    // this.performSearch()
    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);
    if (params.get("query")) {
      this.query = params.get("query");
      this.performSearch();
    }
  },
  methods: {
    async performSearch() {
      this.$store.commit("setLoading", true);

      await axios
        .post(`api/v1/store/search/`, { query: this.query })
        .then((response) => {
          this.books = response.data;
          document.title = "Search | BookStore";
          console.log(this.books);
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setLoading", false);
    },
  },
};
</script>