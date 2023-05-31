<template>
  <div class="background p-3 ml-5">
    <h1>게시글 작성</h1>
    <hr>
    <form @submit.prevent="ArticleCreateView">
      <label for="article_title">제목 : </label>
      <input type="text" id="article_title" v-model="title"><br>
      <label for="article_content">내용 : </label>
      <textarea id="article_content" cols="30" rows="10" v-model="content"></textarea><br>
      <button>등록 </button>
      <router-link :to="{ name : 'community' }"> 뒤로</router-link>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleCreateView',
  data() {
    return {
      title: null,
      content: null
    }
  },
  methods: {
   ArticleCreateView() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: {
          title,
          content
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          // console.log(res)
          this.$router.push({name: 'community'})
        })
        .catch(err => console.log(err))
    }
  }
  
}
</script>

<style>
#article_title{
  font-size: 20px;
}
#article_content{
  font-size: 20px;
}
</style>