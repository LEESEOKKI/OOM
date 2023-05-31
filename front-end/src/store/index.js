import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

const API_URL = 'http://127.0.0.1:8000'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    articles: [],
    movies: [],
    kobises: [],
    details: [],
    genres: [],
    token: null,
    username: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    GET_ARTICLES(state, articles){
      state.articles = articles
      console.log(articles)
    },
    DELETE_ARTICLE(state, article_id){
      state.articles = state.articles.filter((article) => {
        return !(article.id === article_id)
      })
    },
    // UPDATE_ARTICLE(state, article_id){
    //   state.articles = state.articles.mpa((article) =>{
    //     if(article === article_id){
    //       article.isCompleted = !article.isCompleted
    //     }
    //     return article
    //   })
    // },
    SAVE_TOKEN(state, token) {
      state.token = token
      console.log(token)
      router.push({name: 'home' })
    },
    SAVE_USERNAME(state, payload) {
      state.username = payload.username
    },
    DELETE_USERNAME(state) {
      state.username = null
    }
    ,
    LOGOUT(state, token) {
      // return state.token = false
      state.token = token
      router.go()
    },
    GET_MOVIES(state, movies){
      state.movies = movies
    },
    GET_KOBISES(state, kobises){
      state.kobises = kobises
    },
    GET_DETAILS(state, details){
      state.details = details
    },
    GET_GENRES(state, genres){
      state.genres = genres
    },
  },
  actions: {
    getArticles(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then(res =>
          context.commit('GET_ARTICLES', res.data)
        )
        .catch(err => console.log(err))
    },
    getMovies(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movielist/`,
      })
        .then((res) => {
          // console.log(res, context)
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {console.log(err)})
    },
    getKobises(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/kobislist/`,
      })
        .then((res) => {
          // console.log(res, context)
          context.commit('GET_KOBISES', res.data)
        })
        .catch((err) => {console.log(err)})
    },
    getDetails(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/nowlist/`,
      })
        .then((res) => {
          // console.log(res, context)
          context.commit('GET_DETAILS', res.data)
        })
        .catch((err) => {console.log(err)})
    },
    getGenres(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/genres/`,
      })
        .then((res) => {
          context.commit('GET_GENRES', res.data)
        })
        .catch((err) => {console.log(err)})
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
          alert('비밀번호 확실한가요?')
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          context.commit('SAVE_USERNAME', payload)
        })
        .catch((err) => {
          console.log(err)
          alert('아이디 및 비밀번호을 확인해봐요')
        })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          context.commit('LOGOUT', res.data.key)
          // context.commit('SAVE_TOKEN', res.data.key)
          context.commit('DELETE_USERNAME')
        })
        .catch(err => console.log(err.request))
    },
    updateArticle(context, payload){
      const title = payload.title
      const content = payload.content
      const article_id = payload.article_id
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/articles/${article_id}/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        },
        data:{
          title,
          content
        }
      })
      .then((res) => {
        console.log(res)
        
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
