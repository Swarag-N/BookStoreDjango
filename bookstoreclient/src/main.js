import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'https://django-book-store-vue.herokuapp.com/'

createApp(App).use(store).use(router, axios).use(router).mount('#app')
