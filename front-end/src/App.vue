<template>
<div>
<header>
	<nav class="navbar navbar-expand-sm navbar-light bg-dark">
		<div class="container-fluid">
			<router-link to="/" class="navbar-brand">
				<img alt="logo" src="./assets/OOM.png" style="height:100px;" />
			</router-link>
			<div class="collapse navbar-collapse">
				<ul class="navbar-nav me-auto">
					<li class="nav-item">
						<router-link to="/" class="nav-link">Home</router-link>
					</li>
					<li class="nav-item">
						<router-link to="/community" class="nav-link">Community</router-link>
					</li>
					<li class="nav-item">
						<router-link to="/recommend" class="nav-link">Recommend</router-link>
					</li>
					<li class="nav-item">
						<router-link :to="{name: 'SignUp'}" class="nav-link">Signup </router-link>
					</li>
					<li class="nav-item">
						<span style="color: white; cursor:pointer;" v-if="islog == true" @click="logOut"  class="nav-link" >Logout {{username}} 기릿</span>
						<span v-else><router-link :to="{name: 'LogIn'}" class="nav-link">LogIn </router-link></span>
					</li>
				</ul>
			</div>
		</div>
	</nav>
</header>
	<main>
		<router-view/>
	</main>
<footer></footer>
</div>
	

</template>

<script>
export default {
	computed: {
		islog(){
			return this.$store.getters.isLogin
		},
		username(){
			return this.$store.state.username
		}
	},
	methods: {
		logOut(){
			this.$store.dispatch('logOut')
		},
	}
}
</script>
<style>

nav .navbar-nav a.nav-link {
  font-weight: bold;
  color: #eff3f8 !important;
}

nav .navbar-nav a.router-link-exact-active {
  color: rgb(241, 237, 32) !important;
}

.navbar-info a {
	font-weight:bold;
	color:#eff3f8 !important;
	text-decoration:none;
}
#logout {
	font-weight:bold;
	color:#b0c44c !important;
	text-decoration:none;
}
#login {
	font-weight:bold;
	color:#eff3f8 !important;
	text-decoration:none;
}

</style>
