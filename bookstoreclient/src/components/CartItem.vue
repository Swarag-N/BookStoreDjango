<template>
  <tr>
    <td>
      <router-link :to="item.book.get_absolute_url">{{
        item.book.name
      }}</router-link>
    </td>
    <td>${{ item.book.price }}</td>
    <td class="has-text-justified">
      <a @click="incrementQuantity(item)"><i class=" fas fa-plus-circle"></i></a>
      <span class="m-3">{{ item.quantity}}</span> 
      <a @click="decrementQuantity(item)"><i class="fas fa-minus-circle"></i></a>
    </td>
    <td>${{ getItemTotal(item).toFixed(2) }}</td>
    <td><button class="delete" @click="removeFromCart(item)"></button></td>
  </tr>
</template>

<script>
export default {
  name: "CartItem",
  props: {
    initialItem: Object,
  },
  data() {
    return {
      item: this.initialItem,
    };
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.book.price;
    },
    decrementQuantity(item) {
      item.quantity -= 1;
      if (item.quantity === 0) {
        this.$emit("removeFromCart", item);
      }
      this.updateCart();
    },
    incrementQuantity(item) {
      item.quantity += 1;
      this.updateCart();
    },
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
    removeFromCart(item) {
      this.$emit("removeFromCart", item);
      this.updateCart();
    },
  },
};
</script>