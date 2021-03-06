<template>
  <div id="register">
    <div class="one">
      <p class="big">星云</p>
      <p class="small">让人才汇集</p>
    </div>
    <div class="two">
      <div class="login-regist">
          <div class="left-container">
            <div class="title"><span>注册</span></div>
            <div class="input-container">
              <input type="text" name="u_username" placeholder="用户名" v-model="username"/>
              <input type="text" name="u_name" placeholder="真实姓名" v-model="name"/>
              <input type="text" name="u_idcard" placeholder="身份证号" v-model="idcard"/>
              <input type="text" name="u_email" placeholder="邮箱" v-model="email"/>
              <input type="password" name="u_password" placeholder="密码" v-model="password"/>
              <input
                type="password"
                name="confirm_password"
                placeholder="确认密码"
              />
            </div>
          </div>
          <div class="right-container">
            <div class="another">
              <a href="login">登录</a>
            </div>
            <div class="action-container">
              <button class="sub" @click="register">注册</button>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import App from "../App.vue";
import axios from 'axios'
import qs from 'qs'
export default {
  components: { App },
  name: "Register",
  data() {
    return {
      username:null,
      name : null,
      idcard : null,
      email : null,
      password : null
    };
  },
  methods: {
    register:function(){
      let data1 = {
        username:this.username,
        name :this.name,
        idcard : this.idcard,
        email : this.email,
        password : this.password
      }
      let data = qs.stringify(data1);
      axios({
        method:'POST',
        url:'http://localhost:8000/user/register/',
        data:data
      })
      .then((res)=>{
        console.log(res);
        if(res.data.status==201){
          alert(res.data.msg);
        }
        else{
          alert(res.data.msg)
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