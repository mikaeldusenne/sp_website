<template>
<!-- <form method="post" action="/login"> -->
  <!--   <h1>Login Form</h1> -->
  <!--   <input type="text" name="id" placeholder="Username" /> -->
  <!--   <input type="password" name="password" placeholder="Password" /> -->
  <!--   <button type="submit" class="btn btn-primary">Login</button> -->
  <!-- </form> -->

<!-- <div class="container"> -->
  <!--   <div class="column is-4 is-offset-4"> -->
    <!--     <h3 class="title">Login</h3> -->
    <!--     <div class="box"> -->
      <!--       <form method="POST" action="/login"> -->
        <!--         <div class="field"> -->
          <!--           <div class="control"> -->
            <!--             <input class="input is-large" type="text" name="name" placeholder="Id" autofocus=""> -->
            <!--           </div> -->
          <!--         </div> -->
        
        <!--         <div class="field"> -->
          <!--           <div class="control"> -->
            <!--             <input class="input is-large" type="password" name="password" placeholder="Password"> -->
            <!--           </div> -->
          <!--         </div> -->
        
        <!--         <button class="button btn btn-primary is-block is-info is-large is-fullwidth">Log in</button> -->
        <!--       </form> -->
      <!--     </div> -->
    <!--   </div> -->
  <!-- </div> -->
<div class="container">
  <div class="card" style="width: 18rem;">
    <form class="form-signin" method="post" action="/login">
      <!-- <div class="form-group"> -->
        <input type="text" class="form-control" name="id" id="inputId" placeholder="id" autofocus="">
        <input type="password" class="form-control" name="password" id="inputPassword" placeholder="Password">
      <!-- </div> -->
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</div>

</template>

<script>
  export default {
  name: 'Login',
  data() {
  return {
  }
  },
  methods: {
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
