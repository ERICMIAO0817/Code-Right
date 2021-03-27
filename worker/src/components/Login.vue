<template>
  <div id="login">
    <div class="one">
      <p class="big">星云</p>
      <p class="small">让人才汇集</p>
    </div>
    <div class="two">
      <div class="login-regist">
          <div class="left-container">
            <div class="title"><span>登录</span></div>
            <div class="input-container">
              <input type="text" name="u_email" placeholder="邮箱" v-model="username"/>
              <input type="password" name="u_password" placeholder="密码" v-model="password"/>
            </div>
            <div class="message-container">
              <span>忘记密码</span>
            </div>
          </div>
          <div class="right-container">
            <div class="another">
              <a href="register">注册</a>
            </div>
            <div class="action-container">
              <button class="sub" @click="login">登录</button>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
export default {
  name: "Login",
  data() {
    return {
      username:null,
      password:null
    };
  },
  methods: {
    login:function(){
      let data1 = {
        username : this.username,
        password : this.password
      };
      let data = qs.stringify(data1);
      axios({
        method:"POST",
        url:'http://localhost:8000/user/login/',
        data:data
      })
      .then((res)=>{
        console.log(res);
        if(res.data.status==203){
          alert(res.data.msg);
        }
        else if(res.data.status==201){
          alert(res.data.msg);
        }
        else if(res.data.status==202){
          alert(res.data.msg);
        }
        else if(res.data.status==200){
          this.$router.push('/homepage');
        }
      })
      .catch((error)=>{
        console.log(error);
      })
    }
  },
};
</script>
<style scoped>
@import '../assets/nebula-login-regist.css';
</style>
