<template>


    <!-- Welcome Text -->


    <div class="container-fuild">


        <div class="row">


            <div class="col col-12 align-items-center justify-content-center">


                <blockquote>


                    &#8220;Welcome {{validUserName}}!&#8221;
                    

                    <footer>


                    <small>


                        <em>&mdash;The Office Office Supply Store.</em>
                        


                    </small>


                    </footer>


                </blockquote>


            </div>


        </div>


    </div>
    <img :src="require('@/assets/office.jpg')" class="card-img-top" style="height: 15rem">













</template>








<script>


import router from '../router'








  export default {


    name: 'Home',


    data: () => ({


      validUserName: "Guest"


    }),


    mounted() {


      this.getUser();


    },





      getUser() {


        if (localStorage.getItem("isAuthenticates")


          && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {


          this.validUserName = JSON.parse(localStorage.getItem("log_user"));


        }


      }


    }


</script>



