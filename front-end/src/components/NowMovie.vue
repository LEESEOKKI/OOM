<template>
    <div class="py-5">
      <div class="container">
          <div class="row row-cols-1 row-cols-sm-2 ">
              <NowMovieItem class="col my-2"
                  v-for="detail in details"
                  :key="detail.id"
                  :detail="detail"
              />
          </div>
      </div>
    </div>
      
</template>

<script>
import NowMovieItem from '@/components/NowMovieItem'

export default {
    name: 'NowMovie',
    components: {
      NowMovieItem,
    },
    computed: {
      details(){
        return this.$store.state.details
      },
    },
    
    
}
</script>

<style>

</style>