<template>
  <div class="product-wrapper">
    <div class="columns is-multiline">
      <div class="column is-4 is-offset-1">
        <figure class="image mb-6">
          <img v-bind:src="book.get_image" />
        </figure>
      </div>

      <div class="column  is-offset-1">
        <h1 class="title">{{ book.name }}</h1>

        <p class="has-text-justified is-family-sans-serif">{{ book.description }}</p>
        
        <h4 class="subtitle">Information</h4>
        <p><strong>Price: </strong>${{ book.price }}</p>

        <div class="field has-addons mt-6">
          <div class="control">
            <input type="number" class="input" min="1" v-model="quantity" />
          </div>

          <div class="control">
            <a class="button is-dark">Add to cart</a>
          </div>
        </div>
      </div>
      <div class="column is-1"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
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
          document.title = this.product.name + " | Djackets";
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>