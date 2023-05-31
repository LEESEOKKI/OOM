<template>
  <div class="background">
    <div id="community_title">
      자유 게시판
      <router-link :to="{ name : 'ArticleCreateView'}">
      [글쓰기]
      </router-link>
    </div>
    <hr>
    <div class="ml-5">
      <ArticleList/>
    
    </div>
    
  </div>

</template>

<script>
import ArticleList from '@/components/ArticleList'

export default {
  name: 'CommunityView',
  components: {
    ArticleList
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({name: 'LogIn'})
      }
    },
  }
}

</script>

<style>
#community_title{
  font-weight: bold;
  margin-left: 30px;
  font-size: 50px;
}
</style>