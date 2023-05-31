<template>
    <div>
    <MovieListItem
          v-for="genre in genres"
          :key="genre.id"
          :genre="genre"
        />
    </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'

export default {
    name: 'MovieList',
    components: {
      MovieListItem,
    },
    computed: {
      genres(){
        return this.$store.state.genres
      }
    },
    
    
}
</script>

<style>

</style>