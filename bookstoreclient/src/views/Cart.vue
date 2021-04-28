<template>
  <div class="cart-wrapper">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Cart</h1>
      </div>
      <!-- {{cart}} -->
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="cartTotalLength">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <th></th>
            </tr>
          </thead>

          <tbody>
            <CartItem
              v-for="item in cart.items"
              v-bind:key="item.book.id"
              v-bind:initialItem="item"
              v-on:removeFromCart="removeFromCart"
            />
          </tbody>
        </table>

        <p v-else>You don't have any products in your cart...</p>
      </div>

      <div class="column is-12 box">
        <h2 class="subtitle">Summary</h2>

        <strong>${{ cartTotalPrice.toFixed(2) }}</strong
        >, {{ cartTotalLength }} items

        <hr />

        <router-link to="/cart/checkout" class="button is-dark"
          >Proceed to checkout</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import CartItem from "@/components/CartItem.vue";
export default {
  name: "Cart",
  data() {
    return {
      cart: {
        items: [],
      },
    };
  },
  components: {
    CartItem,
  },
  methods:{
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.book.id !== item.book.id)
        }
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.book.price * curVal.quantity);
      }, 0);
    },
  },
};
</script>