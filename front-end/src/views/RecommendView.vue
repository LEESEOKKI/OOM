<template>
  <div class="main background1">
    <div class="d-flex justify-content-center pt-5">
      <div id="community_title"> 추천 영화 목록 </div>
    </div>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
export default {
    name: 'RecommendView',
    components: {
      MovieList
    },
    created(){
      this.getMovies()
      this.getGenres()
    },
    methods: {
      getMovies(){
        this.$store.dispatch('getMovies')
      },
      getGenres(){
        this.$store.dispatch('getGenres')
      },
    }
}
</script>

<style>
.background1 {
	background-color: black;
	background: linear-gradient(to right, transparent, black);
	height: cover !important;
}
</style>