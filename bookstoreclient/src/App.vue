<template>
  <div class="wraperconatiner">
    <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>Book Store</strong>
        </router-link>

        <a
          role="button"
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div
        id="navbar-menu"
        class="navbar-menu"
        v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-end">
          <router-link to="/su" class="navbar-item">Asdasda</router-link>
          <router-link to="/su1" class="navbar-item">Eddsfd</router-link>
          <router-link to="/su3" class="navbar-item">Qsdff</router-link>

          <div class="navbar-item">
            <router-link to="login" class="button is-success">
              <i class="fas fa-sign-in-alt"></i>
              <span>   Login</span></router-link
            >
            </div>
          <div class="navbar-item">
            <router-link to="cart" class="button is-success">
              <span> <i class="fas fa-shopping-cart"></i></span>
              <span>Cart ({{ cartItemsCount }})</span>
            </router-link>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view />
    </section>
    <footer class="footer">
      <div class="content has-text-centered">
        <p>
          <strong>Book Store</strong>
          <br />
          Copyright 2021
        </p>
      </div>
    </footer>
  </div>
</template>

<style lang="scss">
@import "../node_modules/bulma";
</style>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      },
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");
  },
  mounted(){
    this.cart = this.$store.state.cart;
  },
  computed: {
    cartItemsCount() {
      return this.cart.items.length;
    },
  },
};
</script>
