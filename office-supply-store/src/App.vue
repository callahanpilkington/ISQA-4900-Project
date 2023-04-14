<template>
  <ul class="nav justify-content-end">
      <div class="EFS">The Office Office Supply Store</div>
      <li class="nav-item active">
          <router-link to="/">Home</router-link> 
      </li>
      <li class="nav-item">
          <router-link to="/inventory">Inventory</router-link>
      </li>
      <li class="nav-item">
          <router-link to="/orders">Orders</router-link>
      </li>
      <li class="nav-item">
          <router-link to="/login">Login</router-link>
      </li>
  </ul>
  <router-view/>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
      authenticated: false,
      dialog: false,
      menu: [
          { title: 'Home', url:"/"},
          { title: 'Inventory', url:"/inventory" },
      ]
  }),
  mounted() {
      apiService.getCustomerList().then(response => {
          this.authenticated = true;
      }).catch(error => {
          if (error.response.status === 401) {
              localStorage.removeItem('isAuthenticates');
              localStorage.removeItem('log_user');
              localStorage.removeItem('token');
              this.authenticated = false;
          }
      });
      console.log('this.authenticated--'+this.authenticated);
  },
  methods: {
      logout() {
          localStorage.removeItem('isAuthenticates');
          localStorage.removeItem('log_user');
          localStorage.removeItem('token');
          this.authenticated = false;
          // router.push('/');
          window.location = "/"
      },
      login() {
          router.push("/auth");
      },
  }
};
</script>

<style lang="scss">
  #app {
      font-family: Avenir, Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #2c3e50;
  }
  #nav {
      padding: 30px;
      background-color: cadetblue;
      
      
      a {
          font-weight: bold;
          color: #2c3e50;
          &.router-link-exact-active {
              color: #42b983;
          }
      }
  }
  .nav {
      padding: 1em;
      background-color: cadetblue;
      
      li {
          font-weight: bold;
          color: #2c3e50;
          list-style: none;
      }


      a {
          color: black;
          padding: .5em;


          &.router-link-exact-active {
              color: #42b983;
          }
      }


      .EFS{
          // margin-right: 33em;
          text-align: center;
          font-weight: bold;
          font-size: 30px;

      }
  }


</style>


