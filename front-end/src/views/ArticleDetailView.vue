<template>
  <div class="background ml-5 p-3">
    <h1>상세정보</h1>
    <hr>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="deleteArticle">삭제 </button>
    <router-link :to="{ name : 'ArticleUpdateView', params : { id : this.article?.id } }"> 수정 </router-link>
    <router-link :to="{ name : 'community' }"> 뒤로</router-link>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  data() {
    return {
      article: null
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
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
        this.article = res.data
      })
      .catch(err => console.log(err))
    },
    deleteArticle(){
        axios({
          method: 'delete',
          url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((res) => {
            this.article = res.data
            this.$store.commit('DELETE_ARTICLE', this.article.id)
            this.$router.push({ name : 'community'})
        })
        .catch(err => console.log(err))

    }
  }
}
</script>