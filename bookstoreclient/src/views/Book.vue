<template>
  <div class="product-wrapper">
    <div class="columns is-multiline">
      <div class="column is-4 is-offset-1">
        <figure class="image mb-6">
          <img v-bind:src="book.get_image" />
        </figure>
      </div>

      <div class="column is-offset-1">
        <h1 class="title">{{ book.name }}</h1>

        <p class="has-text-justified is-family-sans-serif">
          {{ book.description }}
        </p>

        <h4 class="subtitle">Information</h4>
        <p><strong>Price: </strong>${{ book.price }}</p>

        <div class="field has-addons mt-6">
          <div class="control">
            <input type="number" class="input" min="1" v-model="quantity" />
          </div>

          <div class="control">
            <a class="button is-dark" id="demoSparkles" @click="addToCart"
              >Add to cart</a
            >
          </div>
        </div>
      </div>
      <div class="column is-1"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// TODO Fix Part-JS
// import  party from "party-js";
// const party = require('party-js');
export default {
  name: "Book",
  data() {
    return {
      quantity: 1,
      book: {},
    };
  },

  mounted() {
    this.getBookDetails();
  },

  methods: {
    getBookDetails() {
      const genere_slug = this.$route.params.genere_slug;
      const book_slug = this.$route.params.book_slug;
      axios
        .get(`api/v1/store/${genere_slug}/${book_slug}/`)
        .then((response) => {
          this.book = response.data;
          document.title = this.book.name + " | BookStore";
        })
        .catch((error) => {
          console.log(error);
        });
    },

    addToCart() {
      // const element = document.getElementById("demoSparkles");

      // party()
      // confetti(element);

      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        book: this.book,
        quantity: this.quantity,
      };

      this.$store.commit("addToCart", item);
    },
  },
};
</script>