<template>
  <div class="home">
    <section class="hero is-halfheight" style="background: rgb(34,193,195);
background: radial-gradient(circle, rgba(34,193,195,1) 0%, rgba(45,253,166,0.9867297260701156) 100%);">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h1 class="title">Book Store</h1>
          <h2 class="subtitle">Your Reading Journey Starts Here</h2>
        </div>
      </div>
    </section>
  </div>
  <br />
  <div class="columns is-multiline">
    <div class="column is-12">
      <h3 class="is-size-3 has-text-centered">Latest Books</h3>
    </div>
    <BookCards v-for="book in latestBooks" v-bind:key="book.id"   v-bind:book="book" />
  </div>
</template>


<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import BookCards from "@/components/BookCards.vue";
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      latestBooks: [],
    };
  },
  components: {
    BookCards,
  },
  mounted() {
    this.getLatestBooks();
    document.title = "Home | BookStore";
  },

  methods: {
    async getLatestBooks() {
      this.$store.commit("setLoading", true);
      await axios
        .get("/api/v1/store/latest-products/")
        .then((response) => {
          this.latestBooks = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setLoading", false);
    },
  },
};
</script>
