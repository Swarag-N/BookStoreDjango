<template>
  <div class="wraperconatiner">
    <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
      <div class="navbar-brand m-2">
        <router-link to="/" exact class="navbar-item">
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
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input
                    type="text"
                    class="input is-rounded"
                    placeholder="What are you looking for?"
                    name="query"
                  />
                </div>

                <div class="control">
                  <button class="button is-success">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="navbar-end p-1">
          <router-link to="/fiction"   class="navbar-item"  exact-path>Fiction</router-link>
          <router-link to="/thriller"  class="navbar-item"  exact-path>Thriller</router-link>

          <div class="navbar-item" v-if="$store.state.isAuthenticated">
            <router-link to="my-account"  class="button is-light"  exact-path>
              <i class="fas fa-user-circle"></i>
              <span class="m-2"> My Account</span></router-link
            >
          </div>
          <div class="navbar-item" v-else>
            <router-link to="log-in"  exact-path class="button is-success">
              <i class="fas fa-sign-in-alt"></i>
              <span class="m-2"> Login</span></router-link
            >
          </div>
          <div class="navbar-item">
            <router-link to="cart" class="button is-success" exact-path>
              <i class="fas fa-shopping-cart"></i>
              <span class="m-2">Cart ({{ cartItemsCount }})</span>
            </router-link>
          </div>
        </div>
      </div>
    </nav>

    <div
      class="is-loading-bar has-text-centered"
      v-bind:class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-dual-ring"></div>
    </div>

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


<script>
import axios from "axios";
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
    const token = this.$store.state.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  computed: {
    cartItemsCount() {
      return this.cart.items.length;
    },
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";


.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
