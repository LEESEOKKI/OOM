<template>
  <div>
    <input type="text" class="input-box" placeholder="  한줄평을 작성해주세요  " v-model="commentItem.content" @keyup.enter="createComment">
    <button v-if="islog == true" class="btn btn-primary btn-create" @click="createComment" >   작성   </button>
    <button v-else class="btn btn-primary btn-create" @click="goLogin">   작성   </button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentForm',
  data() {
    return {
      commentItem: {
        content: null,
      }
    }
  },
  computed: {
		islog(){
			return this.$store.getters.isLogin
		},
	},
  props: {
    detail: Object,
  }
  ,
  methods: {
    createComment() {
      const commentItemSet = {
        commentItem: this.commentItem,
        detail: this.detail,
      }
      // const API_URL = 'http://127.0.0.1:8000'
      // if (this.isLogin) {
      //   axios({
      //   method: 'POST',
      //   url: `${API_URL}/api/v1/nowlist/${commentItemSet.detail.id}/comments/`,
      //   data: commentItemSet.commentItem,
      //   })
      //   .then((res) => {
      //     console.log(res.data)
      //     this.$router.go()
      //    })
      //   .catch(err => console.log(err))
      //     this.commentItem.content = null
      //   } else {
      //   alert('로그인이 필요한 서비스 입니다.')
      //   this.$router.push({name: 'LogIn'})
      //   }
      const API_URL = 'http://127.0.0.1:8000'
     
      axios({
      method: 'POST',
      url: `${API_URL}/api/v1/nowlist/${commentItemSet.detail.id}/comments/`,
      data: commentItemSet.commentItem,
      })
      .then((res) => {
        console.log(res.data)
        this.$router.go()
        })
      .catch(err => console.log(err))
        this.commentItem.content = null
      
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
