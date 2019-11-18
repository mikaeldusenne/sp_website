<template>
    <div class="login container">
        <h1>Login</h1>
        <div class="alert-danger">{{error}}</div>
        <div class="card" style="width: 18rem;">
            
            <form class="form-signin" method="post" action="/login" v-on:submit.prevent>
                <!-- <div class="form-group"> -->
                <input type="text" class="form-control" v-model="login.id" id="inputId" placeholder="id" autofocus="">
                <input type="password" class="form-control" v-model="login.password" id="inputPassword" placeholder="Password">
                <!-- </div> -->
                <button class="btn btn-primary" v-on:click="submit">Submit</button>
            </form>
        </div>
    </div>

</template>

<script>
 import axios from 'axios';

 export default {
     name: 'home',
     //components: {
     //LoginForm
     //}
     data() {
         return {
             error: "",
             login: {
                 id : "",
                 password : ""
             }
         }
     },
     methods: {
         submit: function(){
             var self = this;
             console.log('submitting login...');
             console.log(this);
             console.log(this.login);
             axios.post('login', this.login, { headers: {  
                 'Content-Type': 'application/json',
                 'Access-Control-Allow-Origin': '*',
                 withCredentials: true }
             }
             )
                  .then(response => {
                      console.log(response.data)
                      this.$store.commit('change', {logged: true})
                      this.$router.push('/')
                  })
                  .catch(e => {
                      console.log(this.login)
                      console.log("#############")
                      console.log(e.response)
                      self.error = e.response.data
                  })
         }
     }

 }
</script>

<style scoped>
 #login {
     width: 500px;
     border: 1px solid #CCCCCC;
     background-color: #FFFFFF;
     margin: auto;
     margin-top: 200px;
     padding: 20px;
 }
 .card {
     margin: 0 auto; /* Added */
     float: none; /* Added */
     margin-bottom: 10px; /* Added */
 }
 
 .form-signin {
     width: 100%;
     max-width: 330px;
     padding: 15px;
     margin: 0 auto;
 }
 .form-signin .checkbox {
     font-weight: 400;
 }
 .form-signin .form-control {
     position: relative;
     box-sizing: border-box;
     height: auto;
     padding: 10px;
     font-size: 16px;
 }
 .form-signin .form-control:focus {
     z-index: 2;
 }
 .form-signin input[type="email"] {
     margin-bottom: -1px;
     border-bottom-right-radius: 0;
     border-bottom-left-radius: 0;
 }
 .form-signin input[type="password"] {
     margin-bottom: 10px;
     border-top-left-radius: 0;
     border-top-right-radius: 0;
 }

</style>



