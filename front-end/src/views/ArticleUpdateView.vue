<template>
  <div class="background p-3 ml-5">
    <h1>게시글 수정</h1>
    <hr>
    <form @submit.prevent="ArticleUpdateView">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <button @click="ArticleUpdate">완료</button>
      <router-link :to="{name: 'ArticleDetailView' }">뒤로</router-link>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleUpdateView',
  data(){
      return{
      title: null,
      content: null
      }
  },
  created(){
    this.getArticleDetail()
  },
  methods:{
    getArticleDetail() {
      console.log(this.$route.params.id)
      axios({
          method: 'get',
          url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
          headers: {
            Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then((res) => {
          console.log(res.data)
          this.title = res.data.title
          this.content = res.data.content
      })
      .catch(err => console.log(err))
    },
    ArticleUpdate(){
      const data = {
        title : this.title,
        content : this.content,
        article_id : this.$route.params.id
      }
      this.$store.dispatch('updateArticle', data)
      this.$router.push({name: 'ArticleDetailView'})
    }
  }
}
</script>

<style>

</style>