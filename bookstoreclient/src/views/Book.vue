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
            <a class="button is-dark p-3" id="confetti" @click="addToCart"
              ><span class="m-1"> Add to Cart</span>
              <i class="fas fa-cart-plus"></i
            ></a>
          </div>
        </div>
      </div>
      <div class="column is-1"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import party from "party-js";
import { toast } from "bulma-toast";

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
    async getBookDetails() {
      this.$store.commit("setLoading", true);

      const genere_slug = this.$route.params.genere_slug;
      const book_slug = this.$route.params.book_slug;

      await axios
        .get(`api/v1/store/${genere_slug}/${book_slug}/`)
        .then((response) => {
          this.book = response.data;
          document.title = this.book.name + " | BookStore";
        })
        .catch((error) => {
          console.log(error);
          this.$router.push("/");
        });

      this.$store.commit("setLoading", false);
    },

    addToCart() {
      const element = document.getElementById("confetti");

      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        book: this.book,
        quantity: this.quantity,
      };

      party.element(element, {
        count: party.variation(50, 0.5),
        angleSpan: party.minmax(60, 120),
        shapes: ["star"],
      });

      this.$store.commit("addToCart", item);

      toast({
        message: "The Book was added to the cart",
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });
    },
  },
};
</script>