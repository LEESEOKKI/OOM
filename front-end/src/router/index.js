import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/CommunityView.vue'
import RecommendView from '@/views/RecommendView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import MovieDetailView from '@/components/MovieDetailView'
import ArticleCreateView from '@/views/ArticleCreateView'
import ArticleDetailView from '@/views/ArticleDetailView'
import ArticleUpdateView from '@/views/ArticleUpdateView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/articleCreateView',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/Article/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: RecommendView
  }, 
  {
    path: '/SignUp',
    name: 'SignUp',
    component: SignUpView
  },
  {
    path: '/LogIn',
    name: 'LogIn',
    component: LogInView
  },
  {
    path:'/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path:'/ArticleUpdateView/:id',
    name:'ArticleUpdateView',
    component: ArticleUpdateView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
