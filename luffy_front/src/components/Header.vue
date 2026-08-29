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
          <span>登录</span>
          <span class="line">|</span>
          <span>注册</span>
        </div>
      </div>


    </div>
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
  /* claude: 去掉固定 1200px 宽度，改为全宽铺满窗口 */
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
  color: #aaa;
  /* claude: slogan 字号调大到 16px */
  font-size: 16px;
  line-height: 40px;
}

/* claude: 修复导航内部浮动导致的 .nav 高度塌陷 */
.nav {
  background-color: white;
  user-select: none;
  /* claude: 去掉固定 1200px 宽度，改为全宽铺满窗口 */
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
  overflow: hidden;
}

.nav ul {
  /* claude: 去掉上下 padding，行高统一 68px，与右侧登录/注册高度对齐 */
  padding: 0;
  float: left;
  line-height: 68px;
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

/* claude: logo 图片固定 40px 高度并垂直居中，避免 vite.svg 原始 47px 撑高导航栏 */
.logo img {
  height: 40px;
  vertical-align: middle;
  cursor: pointer;
}

.ele {
  margin: 0 20px;
}

.ele span {
  display: block;
  /* claude: 导航字体 18px，行高统一 68px 与导航栏整体高度一致 */
  /* claude: 导航字体调大到 24px */
  font: 24px/68px '微软雅黑';
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
  /* claude: 登录/注册字体与导航项统一为 18px，保持比例协调 */
  /* claude: 登录/注册字体调大到 24px */
  font-size: 24px;
  line-height: 68px;
  cursor: pointer;
}
</style>