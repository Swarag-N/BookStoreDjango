import { createRouter, createWebHistory } from "vue-router";

import store from '../store'

import Home from "../views/Home.vue";
import Book from "../views/Book.vue";
import Genre from "../views/Genre.vue";
import Search from "../views/Search.vue";
import Cart from "../views/Cart.vue";
import SignUp from "../views/SignUp.vue";
import LogIn from "../views/LogIn.vue";
import Account from "../views/Account.vue";
import CheckOut from "../views/CheckOut.vue";
import Success from "../views/Success.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/cart",
    name: "Cart",
    component: Cart,
  },
  {
    path: "/search",
    name: "Search",
    component: Search,
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUp,
  },
  {
    path: "/log-in",
    name: "LogIn",
    component: LogIn,
  },
  {
    path: "/my-account",
    name: "MyAccount",
    component: Account,
    meta: {
      loginRequired: true,
    },
  },
  {
    path: "/cart/checkout",
    name: "CheckOut",
    component: CheckOut,
    meta: {
      loginRequired: true,
    },
  },
  {
    path: "/cart/success",
    name: "Success",
    component: Success,
  },
  {
    path: "/:genere_slug",
    name: "Genres",
    component: Genre,
  },
  {
    path: "/:genere_slug/:book_slug",
    name: "Book",
    component: Book,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.loginRequired) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})
export default router;
