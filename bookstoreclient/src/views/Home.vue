<template>
  <div class="home">
    <section class="hero is-dark is-halfheight">
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

    <!-- <div
      class="column is-multiline is-3"
      v-for="book in latestBooks"
      v-bind:key="book.id"
    >
      <div class="card">
        <div class="card-image">
          <figure class="image is-2by3">
            <img
              v-bind:src="book.get_thumbnail"
              v-bind:alt="book.name"
              srcset=""
            />
          </figure>
        </div>
        <div class="card-content">
          <p class="tittle">
            {{ book.name }}
          </p>
          <p class="subtitle">
            {{ book.author_name }}
          </p>
        </div>
        <div class="card-footer">
          <div class="card-footer-item">
            <router-link v-bind:to="book.get_absolute_url">
              <button class="button is-light">View Details</button></router-link
            >
          </div>

          <p class="card-footer-item">
            <span class="has-text-grey"> Price {{ book.price }} </span>
          </p>
        </div>
      </div>
    </div> -->
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
