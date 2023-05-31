<template>
  <div>
    <CommentListItem
      v-for="(comment, idx) in comments"
      :key="idx"
      :comment="comment"
      :detail="detail"
    />

  </div> 
</template>

<script>
import axios from 'axios'

import CommentListItem from '@/components/CommentListItem'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentList',
  components: {
    CommentListItem
  },
  data(){   
    return {
        comments : []
    }    
  },
  props: {
    detail: Object
  },
  created(){
    // this.getComments()
  },
  watch:{
    detail(newDetail){
        axios({
        method: 'get',
        url: `${API_URL}/api/v1/${newDetail?.id}/comments/`,
      })
      .then((res) => {
        this.comments = res.data
        // console.log(this.commments)
        
      })
      .catch((err) => {console.log(err)})
    }
  },
  methods: {
    getComments(detail){ 
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/${detail?.id}/comments/`,
      })
      .then((res) => {
        this.comments = res.data
        // console.log(this.commments)
      })
      .catch((err) => {console.log(err)})
    }
  },  
}
</script>

<style>

</style>
