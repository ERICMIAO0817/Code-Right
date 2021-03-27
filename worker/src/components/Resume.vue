<template class="body">
  <div id="resume">
    <div class="people-list"></div>
    <div class="ability">
      <div class="pic"><img v-bind:src="KPI" alt="KPI折线图" /></div>
      <div class="pic">
        <img v-bind:src="conclude" alt="个人多项能力得分" />
      </div>
    </div>
    <div class="top">
      <img v-bind:src="photo" class="id-photo" />
      <div class="information">
        <div class="part">
          姓名:&nbsp;&nbsp;&nbsp;&nbsp;<span>{{ this.name }}</span>
        </div>
        <div class="part">
          性别:&nbsp;&nbsp;&nbsp;&nbsp;<span>{{ this.sex }}</span>
        </div>
        <div class="part">
          年龄:&nbsp;&nbsp;&nbsp;&nbsp;<span>{{ this.age }}</span>
        </div>
        <div class="part">
          邮箱:&nbsp;&nbsp;&nbsp;&nbsp;<span>{{ this.email }}</span>
        </div>
        <div class="part">
          工龄:&nbsp;&nbsp;&nbsp;&nbsp;<span>{{ this.workage }}</span>
        </div>
      </div>
    </div>
    <div class="pic-left"><img v-bind:src="join" alt="项目完成度" /></div>
    <div class="experience">
      <div class="exp">
        <h3><img class="small" src="../assets/image/school.png" /> 教育经历</h3>
        <p>{{ this.education }}</p>
      </div>
      <div class="exp">
        <h3><img class="small" src="../assets/image/work.png" /> 工作经历</h3>
        <p>{{ this.workexp }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "../assets/resume.css";
</style>
<script>
import axios from "axios";
export default {
  name: "Resume",
  data() {
    return {
      id: 1,
      name: "Eric",
      photo: null,
      sex: null,
      age: null,
      email: null,
      workage: null,
      education: null,
      workexp: null,
      conclude: null,
      join: null,
      KPI: null,
    };
  },
  methods: {
    getResume: function () {
      let data1 = {
        name: this.name,
      };
      axios({
        method: "GET",
        url: "http://localhost:8000/resume/getResume",
        params: {
          name: this.name,
        },
      }).then((res) => {
        console.log(res);
        this.name = res.data.name;
        if (res.data.sex == false) {
          this.sex = "男";
        } else {
          this.sex = "女";
        }
        // this.sex = res.data.sex;
        this.age = res.data.age;
        this.photo = res.data.photo;
        this.email = res.data.email;
        this.workage = res.data.work_age;
        this.education = res.data.education;
        this.workexp = res.data.experience;
        this.conclude = res.data.pic3;
        this.join = res.data.pic2;
        this.KPI = res.data.pic1;
      });
    },
  },
  mounted: function () {
    this.getResume();
  },
};
</script>