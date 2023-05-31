<template>
    <div>
        <b-card no-body class="overflow-hidden" style="max-width: 540px;">
            <b-row no-gutters>
            <b-col md="6">
                <b-card-img
        :src="detail.poster_path"
        @click="toDetail" class="rounded-0">
        </b-card-img>
            </b-col>
            <b-col md="6">
                <b-card-body>
                    <b-card-text>
                        <div id="title1">
                            <span v-for="(kobis,i) in kobises" :key="i">
                                <div v-if="kobis.id == detail.id" class="card-title">
                                    {{kobis.name.split('\n', 1)[0]}}
                                </div>
                            </span>
                        </div>
                        <hr>
                        <div id="font" >
                            <span v-for="(kobis,i) in kobises" :key="i">
                                <div v-if="kobis.id == detail.id" class="card-title">
                                    어제 관객 수 {{kobis.spectators.split('\n', 1)[0]}}
                                </div>
                            </span>
                        </div>
                        <p>{{detail.movie_detail.split('|',6)[2]}}</p>
                        <p>{{detail.movie_detail.split('|',6)[3].split(' ',2)[1]}}</p>
                        <p>{{detail.movie_detail.split('|',6)[4]}}</p>
                        <p>{{detail.movie_detail.split('|',6)[5]}}</p>
                    </b-card-text>
                </b-card-body>
            </b-col>
            </b-row>
        </b-card>
    </div>
</template>

<script>

export default {
    name: 'NowMovieItem',

    props: {
        detail: Object,
    },
    methods: {
      toDetail(){
        this.$router.push({name: 'MovieDetailView', params: {id: this.detail.id}})
      }
    },
    computed: {
      kobises(){
        return this.$store.state.kobises
      },
    },
}
</script>

<style>
/* b-card{
    position: absolute;
    object-fit: cover;
} */
.imgSize {
    width: 250;
    height: 370;
    object-fit: cover !important;
}
.card-img-top {
  height: 15em;
  object-fit: scale-down;
}
#title1{
    font-size: 26px;
    font-weight: bold;
    color: #7F6AF7;
}
#font{
    color: gold;
    font-size: 25px;
    font-weight: bold;
    font-family: sans-serif;
    animation: blink-effect 1s step-end infinite;
}
@keyframes blink-effect {
  50% {
    opacity: 0;
  }
}
</style>