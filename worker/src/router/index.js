import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import Resume from '../components/Resume.vue'
import Index from '../components/Index.vue'
import Question from '../components/question.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/user/resume',
      name: 'Resume',
      component: Resume
    },
    {
      path: '/index',
      name: 'Index',
      component: Index
    },
    {
      path:'/user/question',
      name:'Question',
      component:Question
    }
  ],
  mode: "history"
})