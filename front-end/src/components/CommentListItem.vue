<template>
  <div v-if="comment?.detail==detail?.id">
    <span>{{ comment?.content }}</span>  
    <button v-if="islog == true" @click="deleteComment">삭제</button>
    
  </div>
</template>

<script>

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentListItem',
  props: {
    comment: {
      type: Object,
    },
    detail: null 
  },
  data() {
    return {
      commentItem: {
        content: this.comment.content
      },
    }
  },
  computed: {
		islog(){
			return this.$store.getters.isLogin
		},
	},
  methods: {
    deleteComment(){ 
      console.log(this.comment.id)
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/comments/${this.comment?.id}/`,
      })
      .then(() => {
        console.log("delete success")
        this.$router.go()

      })
      .catch((err) => {console.log(err)})
    },
    goLogin(){
      alert('로그인이 필요합니다.')
      this.$router.push({name: 'LogIn'})
    }  
  },
}
</script>

<style>

</style>
