import { createApp } from 'vue'
import App from './App.vue'
import axios from "axios";

import router from './router'
import store from './store'

axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://localhost:5000/'   // backend fastapi

createApp(App).use(router).use(store).mount('#app')
