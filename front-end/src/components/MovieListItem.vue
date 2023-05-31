<template>
    <div class="py-5">
      <div class="container">
        <div>
            <vue-flashcard class="col my-2"
            :front="genre?.name"
            :back="randomitem?.title"
            :imgBack="imgUrl+randomitem?.poster_path">
            </vue-flashcard>
        </div>
      </div>
    </div>
    
</template>

<script>
import vueFlashcard from 'vue-flashcard'

export default {
    props: {
        genre: Object
    },
    components: {
        vueFlashcard,
    },
    data(){
        return {
            imgUrl: 'https://image.tmdb.org/t/p/w500',
            randomitem: this.genre.tmdbs[Math.floor(Math.random() * this.genre.tmdbs.length)]
        }
    },
    name: 'MovieListItem',
}
</script>

<style>
b-card{
    position: absolute;
    object-fit: cover;
}
.imgSize {
    width: 246;
    height: 370;
    object-fit: cover !important;
}
</style>