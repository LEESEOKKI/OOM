<template>
<div class="background">
  <div class="container pt-5">
    <div class="row justify-content-center">
      <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
        <div class="card">
          <div class="card-header">
            <h4>SignUp</h4>
          </div>
          <div class="card-body">
            <form @submit.prevent="signUp" class="form-group">
              <input type="text" id="username" v-model="username" placeholder="username" class="form-control form-control-lg"><br>

              <input type="password" id="password1" v-model="password1" placeholder="password" class="form-control form-control-lg"><br>

              <input type="password" id="password2" v-model="password2" placeholder="password confirm" class="form-control form-control-lg">
              <br>
              <input type="submit" value="SignUp" class="btn btn-primary">
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
    name: 'SignUpView',
    data() {
      return {
        username: null,
        password1: null,
        password2: null,
      }
    },
    methods: {
      signUp() {
        const username = this.username
        const password1 = this.password1
        const password2 = this.password2

        const payload = {
          username: username,
          password1: password1,
          password2: password2,
        }
        this.$store.dispatch('signUp', payload)
      }
    }
}
</script>

<style>
.background {
	background-color: black;
	background: linear-gradient(to right, transparent, black);
	
}
</style>