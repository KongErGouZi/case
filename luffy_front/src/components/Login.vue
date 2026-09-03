<template>
  <div class="login">
    <div class="box">
      <i class="el-icon-close" @click="close_login">
        <el-icon :size="size" :color="color">
          <Close/>
        </el-icon>
      </i>
      <div class="content">
        <div class="nav">
                    <span :class="{active: login_method === 'is_pwd'}"
                          @click="change_login_method('is_pwd')">密码登录</span>
          <span :class="{active: login_method === 'is_sms'}"
                @click="change_login_method('is_sms')">短信登录</span>
        </div>
        <el-form v-if="login_method === 'is_pwd'">
          <el-input
              placeholder="用户名/手机号/邮箱"
              :prefix-icon="User"
              v-model="username"
              clearable>
          </el-input>
          <el-input
              placeholder="密码"
              :prefix-icon="Lock"
              v-model="password"
              clearable
              show-password>

          </el-input>
          <el-button type="primary">登录</el-button>
        </el-form>
        <el-form v-if="login_method === 'is_sms'">
          <el-input
              placeholder="手机号"
              :prefix-icon="Iphone"
              v-model="mobile"
              clearable
              @blur="check_mobile">
          </el-input>
          <el-input
              placeholder="验证码"
              :prefix-icon="ChatLineRound"
              v-model="sms"
              clearable>
            <template slot="append">
              <span class="sms" @click="send_sms">{{ sms_interval }}</span>
            </template>
          </el-input>
          <el-button type="primary">登录</el-button>
        </el-form>
        <div class="foot">
          <span @click="go_register">立即注册</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref} from "vue";
import {ElMessage} from "element-plus";
//小图标引入
import {User, Lock, Iphone, ChatLineRound} from '@element-plus/icons-vue'

let $emit = defineEmits(['close', 'go'])

const close_login = () => {
  // 通知父组件 close，父组件监听 close 事件，然后执行绑定 close 事件的函数
  $emit('close')
}

const go_register = () => {
  $emit('go')
}


</script>

<style scoped>
.login {
  width: 100vw;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 10;
  background-color: rgba(0, 0, 0, 0.8);
}

.box {
  width: 400px;
  height: 420px;
  background-color: white;
  border-radius: 10px;
  position: relative;
  top: calc(50vh - 210px);
  left: calc(50vw - 200px);
}

.el-icon-close {
  position: absolute;
  font-weight: bold;
  font-size: 20px;
  top: 10px;
  right: 10px;
  cursor: pointer;
}

.el-icon-close:hover {
  color: darkred;
}

.content {
  position: absolute;
  top: 40px;
  width: 280px;
  left: 60px;
}

.nav {
  font-size: 20px;
  height: 38px;
  border-bottom: 2px solid darkgrey;
}

.nav > span {
  margin: 0 20px 0 35px;
  color: darkgrey;
  user-select: none;
  cursor: pointer;
  padding-bottom: 10px;
  border-bottom: 2px solid darkgrey;
}

.nav > span.active {
  color: black;
  border-bottom: 3px solid black;
  padding-bottom: 9px;
}

.el-input, .el-button {
  margin-top: 40px;
}

.el-button {
  width: 100%;
  font-size: 18px;
}

.foot > span {
  float: right;
  margin-top: 20px;
  color: orange;
  cursor: pointer;
}

.sms {
  color: orange;
  cursor: pointer;
  display: inline-block;
  width: 70px;
  text-align: center;
  user-select: none;
}
</style>