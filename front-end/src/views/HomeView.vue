<template>
  <div class="background">
	
		<b-carousel
			id="carousel-fade"
			style="text-shadow: 0px 0px 2px #000"
			fade
			img-width="1024"
			img-height="480"

		>
			<b-carousel-slide class="main"
			:img-src="this.$store.state.details[Math.floor(Math.random() * this.$store.state.details.length)].poster_path"
			></b-carousel-slide>
			<b-carousel-slide class="main"
			:img-src="this.$store.state.details[Math.floor(Math.random() * this.$store.state.details.length)].poster_path"
			></b-carousel-slide>
			<b-carousel-slide class="main"
			:img-src="this.$store.state.details[Math.floor(Math.random() * this.$store.state.details.length)].poster_path"
			></b-carousel-slide>
			<b-carousel-slide class="main"
			:img-src="this.$store.state.details[Math.floor(Math.random() * this.$store.state.details.length)].poster_path"
			></b-carousel-slide>
			<b-carousel-slide class="main"
			:img-src="this.$store.state.details[Math.floor(Math.random() * this.$store.state.details.length)].poster_path"
			></b-carousel-slide>
			<b-carousel-slide class="main"
			:img-src="this.$store.state.details[Math.floor(Math.random() * this.$store.state.details.length)].poster_path"
			></b-carousel-slide>
			<b-carousel-slide class="main"
			:img-src="this.$store.state.details[Math.floor(Math.random() * this.$store.state.details.length)].poster_path"
			></b-carousel-slide>
			<b-carousel-slide class="main"
			:img-src="this.$store.state.details[Math.floor(Math.random() * this.$store.state.details.length)].poster_path"
			></b-carousel-slide>
		</b-carousel>
		<div id="subject">오늘 영화는 무엇인가요?</div>
		<NowMovie/>
	
</div>
</template>

<script>
// @ is an alias to /src
import NowMovie from '@/components/NowMovie'

export default {
	name: 'HomeView',
	components: {
		NowMovie
	},
	created(){
		this.getDetails()
		this.getKobises()
	},
	computed: {
		islog(){
			return this.$store.getters.isLogin
		},
		username(){
			return this.$store.state.username
		},
	},
	methods: {
		logOut(){
			this.$store.dispatch('logOut')
		},
		getDetails(){
			this.$store.dispatch('getDetails')
		},
		getKobises(){
			this.$store.dispatch('getKobises')
		}
	},
}
</script>

<style>
.main {
  position: relative;
  width: 100%;
  background-color: rgb(41, 25, 58);
}
.background {
	background-color: black;
	background: linear-gradient(to right, transparent, black);
	height: 2730px;
}
#carousel-fade {
height: 200px;;
min-height: 200px;
background: no-repeat center center scroll;
-webkit-background-size: cover;
-moz-background-size: cover;
-o-background-size: cover;
background-size: cover;
z-index: -1;
}
#subject{
	font-size: 100px;
	z-index: 1;
	color: white;
	margin-left: 400px;

}
</style>