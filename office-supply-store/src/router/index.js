import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/Home.vue'
// import Auth from '@/components/Auth.vue'
import Inventory from '@/components/Inventory.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/inventory',
    name: 'Inventory',
    component: Inventory
  },
]
  const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  })
  
  export default router
