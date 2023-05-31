<template id="no-scroll">
  <div id="no-scroll">
    <!-- <div class="main my_bg" v-bind:style="{backgroundImage: 'url('+detail?.poster_path+')'}"> -->
    <img :src="detail?.poster_path" id="back">
      <div style="background: linear-gradient(to left, transparent, rgb(6,6,6)); height: 2725px;">
        <div id="text">
          <span v-for="(kobis,i) in kobises" :key="i">
            <div v-if="(kobis?.id == detail?.id)">
                {{kobis?.name.split('\n', 1)[0]}}
            </div>
          </span>
          <div id="content1">
            {{detail?.movie_detail}}
          </div>
          <br>
          <span v-for="(kobis,idx) in kobises" :key="`o-${idx}`">
            <h4 v-if="(kobis?.id == detail?.id)">
                개봉일 : {{kobis?.open_data.split('\n', 1)[0]}}<br><br>
                누적관객수 : {{kobis?.spectators_total.split('\n', 1)[0]}} 명<br><br>
                평점 : 💗{{kobis?.average}}<br><br>
            </h4>
          </span><br>
          <hr>
          <div id="content1">상세정보
            <div id="overview">
              <span v-for="(kobis,i) in kobises" :key="i">
                <div v-if="(kobis?.id == detail?.id)">
                    {{kobis?.overview.split('\n', 1)[0]}}
                </div>
              </span>
            </div>
          <br>
          <hr>
          <br>
          한줄평
          <br>
            <CommentForm
          :detail="detail"
          />
          <br>
          <CommentList
          :detail="detail"
          /> 
          </div>
          <div id="comment_size">
          </div>
        </div>
    </div>
  </div>
 <!-- </div> -->

</template>

<script>
import CommentForm from '@/components/CommentForm'
import CommentList from '@/components/CommentList'

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'MovieDetailView',
    data(){
        return {
          detail: null,
          kobis: null,
        }
    },
    components: {
      CommentForm,
      CommentList,
    },
    computed: {
      details(){
        return this.$store.state.details
      },
      kobises(){
        return this.$store.state.kobises
      }
    },
    created(){
      this.getMovieDetail()
    },
    mounted() {
      window.scrollTo(0, 0);
      document.addEventListener('scroll', this.scrollEvents);
    },
    methods: {
      getMovieDetail(){
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/nowlist/${this.$route.params.id}`
        })
         .then(res => {
            this.detail = res.data
          })
          .catch((err) =>{
            console.log(err)
          })
      }
    }
}
</script>

<style>
/* .my_bg{
  background: linear-gradient(to left, transparent, mistyrose),
  url(https://img.danawa.com/prod_img/500000/783/445/img/13445783_1.jpg?shrink=330:330&_v=20210714124847);
  background-repeat : no-repeat;
  background-size : cover;
} */
#back{
  background: linear-gradient(to left, transparent, rgb(6,6,6));
  position: absolute;
  width: 100%;
  z-index: -1;
}
#text{
  color: white;
  position: absolute;
  letter-spacing: 5px;
  font-weight: bold;
  font-size: 60px;
  left: 200px;
  top: 350px;
  right: 200px;
}
#content1{
  margin-top: 30px;
  font-size: 30px;
}
#no-scroll {
    overflow: hidden !important
}
hr{
  background: white;
  height: 1px;
  border: 0;
}
#overview{
  margin-top: 50px;
  font-size: 25px;
}

</style>