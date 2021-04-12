<template>
  <div id="select">
        <!--导航栏-->
        <div class="top_Style">
            <div class="top_logo">
                <img src="../assets/image/星云0.png" alt="星云logo">
            </div>
            <div class="search">
                <form action="">
                    <input type="text" placeholder="请输入您要搜索的姓名...">
                    <button type="submit"></button>
                </form>
            </div>
            <div class="top_Register">
                <a href="#" class="top_a">评分标准</a>
                <a href="#" class="top_a">我的</a>
            </div>
        </div>
        <!--筛选表格-->
        <div class="box">
            <table>
                <thead>
                    <tr>
                        <td>姓名</td>
                        <td>性别</td>
                        <td v-for="h in tableHeads">{{h}}
                            <div class="arr">
                                <div @mouseover="ontriangle1(h)" @mouseout="offtriangle()" :class="{arr2 : true, arrUp1 : triangle == 'mouseout', arrUp2 : triangle == h+'up'}"></div>
                                <div @mouseover="ontriangle2(h)" @mouseout="offtriangle()" :class="{arr2 : true, arrDown1 : triangle == 'mouseout', arrDown2 : triangle == h+'down'}"></div>
                            </div>
                        </td>
                    </tr>
                </thead>
                <tbody>
                    <!-- 可以点击一行跳转到简历页面，但目前让它跳转到百度了 -->
                    <tr onclick="location.href='https://www.baidu.com/'" v-for="(v,i) in peoples" :key="i" @mouseover="selected(v.name)" @mouseout="unselected()" :class="{dark : active == 'mouseout', light : active == v.name}">
                        <td>{{v.name}}</td>
                        <td>{{v.sex}}</td>
                        <td>{{v.age}}</td>
                        <td>{{v.KPI}}</td>
                        <td>{{v.join}}</td>
                        <td>{{v.time}}</td>
                        <td>{{v.attend}}</td>
                        <td>{{v.score}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    name:"select",
    data() {
        return{
            tableHeads: ['年龄', 'KPI', '项目参与度', '上家公司在任时长', '出勤率', '综合评分'], //每个应该再设置一个index，使非事件对象保持原状
            peoples: [{
                name: '杨睿',
                sex: '女',
                age: 19,
                score: 98,
                KPI: 100,
                join: 0.3,
                time: 3,
                attend: 0.9,
            }, {
                name: '五条悟',
                sex: '男',
                age: 27,
                score: 99,
                KPI: 70,
                join: 0.1,
                time: 7,
                attend: 0.2,
            }, {
                name: '狗卷棘',
                sex: '男',
                age: 18,
                score: 85,
                KPI: 90,
                join: 0.5,
                time: 5,
                attend: 0.5,
            },{
                name: '东堂葵',
                sex: '男',
                age: 27,
                score: 99,
                KPI: 70,
                join: 0.1,
                time: 7,
                attend: 0.2,
            }, {
                name: '罗云熙',
                sex: '男',
                age: 18,
                score: 85,
                KPI: 90,
                join: 0.5,
                time: 5,
                attend: 0.5,
            },{
                name: '花御',
                sex: '男',
                age: 27,
                score: 99,
                KPI: 70,
                join: 0.1,
                time: 7,
                attend: 0.2,
            }, {
                name: '陈飞宇',
                sex: '男',
                age: 18,
                score: 85,
                KPI: 90,
                join: 0.5,
                time: 5,
                attend: 0.5,
            },{
                name: '陈彦宇',
                sex: '男',
                age: 27,
                score: 99,
                KPI: 70,
                join: 0.1,
                time: 7,
                attend: 0.2,
            }, {
                name: '苗子阳',
                sex: '男',
                age: 18,
                score: 85,
                KPI: 90,
                join: 0.5,
                time: 5,
                attend: 0.5,
            },{
                name: '苗李阳',
                sex: '男',
                age: 27,
                score: 99,
                KPI: 70,
                join: 0.1,
                time: 7,
                attend: 0.2,
            }, {
                name: '谌怀义',
                sex: '男',
                age: 18,
                score: 85,
                KPI: 90,
                join: 0.5,
                time: 5,
                attend: 0.5,
            },{
                name: '常佳宇',
                sex: '女',
                age: 27,
                score: 99,
                KPI: 70,
                join: 0.1,
                time: 7,
                attend: 0.2,
            }, {
                name: '真人',
                sex: '男',
                age: 18,
                score: 85,
                KPI: 90,
                join: 0.5,
                time: 5,
                attend: 0.5,
            },{
                name: '熊猫',
                sex: '男',
                age: 27,
                score: 99,
                KPI: 70,
                join: 0.1,
                time: 7,
                attend: 0.2,
            }, {
                name: '夏油杰',
                sex: '男',
                age: 18,
                score: 85,
                KPI: 90,
                join: 0.5,
                time: 5,
                attend: 0.5,
            }],
            triangle: 'mouseout',
            active: 'mouseout',
            click: false,
        };
        
    },
    methods:{
        ontriangle1(name) {
            this.triangle = name + 'up';
        },
        ontriangle2(name) {
            this.triangle = name + 'down';
        },
        offtriangle() {
            this.triangle = 'mouseout';
        },
        selected(name) {
            this.active = name;
        },
        unselected() {
            this.active = 'mouseout';
        },
    }
}
</script>

<style scoped>
.top_Style {
    display: flex;
    justify-content: space-between;
    width: 100%;
    height: 60px;
}       
.top_logo {
    width: 120px;
    height: 60px;
    margin-left: 40px;
}
.top_logo img {
    width:120px;
    height:60px;
}
form {
    position: relative;
    width: 300px;
    height: 42px;
    margin: 0 auto;
}

.search {
    padding: 10px 0;
    font-weight: 500;
    font-family: "Microsoft YaHei", "宋体", "Segoe UI", "Lucida Grande", Helvetica, Arial, sans-serif, FreeSans, Arimo;
}

button {
    /*隐藏按钮*/
    display: none;
    background: none;
    top: 3px;
    right: 0;
    height: 42px;
    width: 42px;
    cursor: pointer;
    position: absolute;
    border: none;
    outline: none;
}

input {
    width: 250px;
    height: 42px;
    padding-left: 13px;
    border-radius: 42px;
    border: 2px solid #324B4E;
    background: #f5fbff;
    transition: .3s linear;
    float: right;
    outline: none;
}

input:focus {
    width: 300px;
}
.top_Register {
    width: 166px;
    height: 60px;
    line-height: 60px;
}

.top_a {
    margin-right: 20px;
    text-decoration: none;
    color: #039BE5;
}

.top_Register a:hover {
    border-bottom: solid 1px #039BE5;
}

.box {
    position: relative;
    margin: 0 auto;
    padding-top: 30px;
    background-color: white;
    width: 870px;
}

table {
    margin: 0px auto;
    border-collapse: collapse;
    table-layout: fixed;
    text-align: center;
    color: rgb(76, 78, 83);
}

thead tr td:nth-child(odd) {
    line-height: 40px;
    background: #f1f1f1;
}

thead tr td:nth-child(even) {
    line-height: 40px;
    background: #f8f8f8;
}

.dark td:nth-child(odd) {
    background: #f7f7f7;
}

.dark td:nth-child(even) {
    background: #fcfcfc;
}

td {
    padding: 10px 20px;
    border-bottom: 1px solid rgb(219, 219, 219);
}

.arr {
    width: 8px;
    position: relative;
    float: right;
    padding-left: 5px;
    padding-top: 2px;
}

.arr2 {
    width: 0;
    height: 0;
    border: 8px solid transparent;
    margin-top: 2px;
    cursor: pointer;
}

.arrUp1 {
    border-bottom-color: #ccc;
}

.arrDown1 {
    border-top-color: #ccc;
}

.arrUp2 {
    border-bottom-color: rgb(56, 55, 55);
}

.arrDown2 {
    border-top-color: rgb(56, 55, 55);
}

.light {
    background-color: rgb(206, 229, 250);
}
</style>