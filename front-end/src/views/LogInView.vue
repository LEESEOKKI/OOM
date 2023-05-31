<template>
  <div class="background main pt-5">
    <div class="row justify-content-center">
      <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
        <div class="card">
          <div class="card-header">
            <h4>LogIn</h4>
          </div>
          <div class="card-body">
             <form @submit.prevent="logIn" class="form-group">
              <input type="text" id="username" v-model="username" placeholder="username" class="form-control form-control-lg"><br>

              <input type="password" id="password" v-model="password" placeholder="password" class="form-control form-control-lg"><br>

              <input type="submit" value="logIn" class="btn btn-primary">
              <router-link :to="{name: 'SignUp'}" class="nav-link">회원이 아니신가요? </router-link>
            </form>
          </div>
        </div>
    </div>
    </div>
  </div>
  

</template>

<script>
export default {
    name: 'LogInView',
    data() {
        return {
            username: null,
            password: null,
        }
    },
    methods: {
        logIn() {
            const username = this.username
            const password = this.password

            const payload = {
                username: username,
                password: password,
            }
            this.$store.dispatch('logIn', payload)
        }
    }

}
</script>

<style>
</style>