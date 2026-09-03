<template>
  <div class="header">
    <div class="slogan">
      <p>老男孩IT教育 | 帮助有志向的年轻人通过努力学习获得体面的工作和生活</p>
    </div>
    <div class="nav">
      <ul class="left-part">
        <li class="logo">
          <img src="../assets/vite.svg" alt="" @click="goPage('/')">

        </li>
        <li class="ele">
          <span @click="goPage('/free-course')" :class="{active: url_path === '/free-course'}">免费课</span>
        </li>
        <li class="ele">
          <span @click="goPage('/actual-course')" :class="{active: url_path === '/actual-course'}">实战课</span>
        </li>
        <li class="ele">
          <span @click="goPage('/light-course')" :class="{active: url_path === '/light-course'}">轻课</span>
        </li>
      </ul>

      <div class="right-part">
        <div>
          <span @click="put_login">登录</span>
          <span class="line">|</span>
          <span @click="put_register">注册</span>
        </div>
      </div>


    </div>
  </div>

  <div>
    <Login v-if="is_login" @close="close_login" @go="put_register"/>
    <Register v-if="is_register" @close="close_register" @go="put_login"/>
  </div>
</template>

<script setup lang="js">
import {useRoute, useRouter} from "vue-router";


// 当前路由信息对象，只读，拿参数、路径、query
let $route = useRoute()
// 路由实例，做跳转、编程式导航
let $router = useRouter()

let url_path = sessionStorage.url_path || '/'

const goPage = (path) => {
  if (url_path !== path) {
    $router.push(path)
  }
  sessionStorage.url_path = path
}

// 登录注册模态框
import Login from "./Login.vue";
import Register from "./Register.vue";
import {ref} from "vue";

const is_login = ref(false)
const is_register = ref(false)

const close_login = () => {
  is_login.value = false
}

const close_register = () => {
  is_register.value = false
}

const put_register = () => {
  is_register.value = true
  is_login.value = false
}

const put_login = () => {
  is_login.value = true
  is_register.value = false
}


</script>

<style scoped>
.header {
  background-color: white;
  box-shadow: 0 0 5px 0 #aaa;
}

.header:after {
  content: "";
  display: block;
  clear: both;
}

.slogan {
  background-color: #eee;
  height: 40px;
}

.slogan p {
  width: 1200px;
  margin: 0 auto;
  color: #aaa;
  font-size: 13px;
  line-height: 40px;
}

.nav {
  background-color: white;
  user-select: none;
  width: 1200px;
  margin: 0 auto;

}

.nav ul {
  padding: 15px 0;
  float: left;
}

.nav ul:after {
  clear: both;
  content: '';
  display: block;
}

.nav ul li {
  float: left;
}

.logo {
  margin-right: 20px;
}

.ele {
  margin: 0 20px;
}

.ele span {
  display: block;
  font: 15px/36px '微软雅黑';
  border-bottom: 2px solid transparent;
  cursor: pointer;
}

.ele span:hover {
  border-bottom-color: orange;
}

.ele span.active {
  color: orange;
  border-bottom-color: orange;
}

.right-part {
  float: right;
}

.right-part .line {
  margin: 0 10px;
}

.right-part span {
  line-height: 68px;
  cursor: pointer;
}
</style>