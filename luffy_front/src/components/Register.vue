<template>
  <div class="register">
    <div class="box">
      <i class="el-icon-close" @click="close_register">
        <el-icon :size="size" :color="color">
          <Close/>
        </el-icon>
      </i>
      <div class="content">
        <div class="nav">
          <span class="active">新用户注册</span>
        </div>
        <el-form>
          <el-input
              placeholder="手机号"
              :prefix-icon="Iphone"
              v-model="mobile"
              clearable
              @blur="checkMobile">
          </el-input>
          <el-input
              placeholder="密码"
              :prefix-icon="Lock"
              v-model="password"
              clearable
              show-password>
          </el-input>
          <el-input
              placeholder="验证码"
              :prefix-icon="ChatLineRound"
              v-model="sms"
              clearable>
            <template #append>
              <span class="sms" @click="sendSms">{{ smsInterval }}</span>
            </template>
          </el-input>
          <el-button type="primary" @click="goRegister">注册</el-button>
        </el-form>
        <div class="foot">
          <span @click="go_login">立即登录</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {User, Lock, Iphone, ChatLineRound} from '@element-plus/icons-vue'
import {ref} from "vue"
import {ElMessage} from "element-plus"
import {reqCheckMobile, reqSendSms, reqRegister} from "../api/user.js"


let $emit = defineEmits(['close', 'go'])

const close_register = () => {
  $emit('close')
}

const go_login = () => {
  $emit('go')
}

// 手机号校验
const mobile = ref('')
const isSend = ref(false)
const checkMobile = async () => {
  if (!mobile.value) return;
  if (!mobile.value.match(/^1[3-9][0-9]{9}$/)) {
    ElMessage({
      type: 'error',
      message: '请输入正确的手机号',
      onClose: () => {
        mobile.value = ''
      }
    })
    return false
  }
  let res = await reqCheckMobile(mobile.value)
  if (!res.is_exist) {
    isSend.value = true
  } else {
    ElMessage({
      type: 'error',
      message: '手机号已经注册过了',
      onClose: () => {
        mobile.value = ''
        go_login()
      }
    })
  }
}

// 短信发送
const smsInterval = ref('')
const sms = ref('')
const sendSms = async () => {
  if (!isSend.value) return;
  isSend.value = false
  let smsIntervalTime = 60
  smsInterval.value = '发送中...'
  let timer = setInterval(() => {
    if (smsIntervalTime <= 1) {
      smsInterval.value = '获取验证码'
      isSend.value = true
    } else {
      smsIntervalTime -= 1
      smsInterval.value = `${smsIntervalTime}秒后重新获取`
    }
  }, 1000)
  await reqSendSms(mobile.value)
}

// 注册
const password = ref('')
const goRegister = async () => {
  if (mobile.value && password.value && sms.value) {
    await reqRegister(mobile.value, sms.value, password.value)
    ElMessage({
      type: 'success',
      message: '注册成功，去登陆吧！',
      onClose: () => {
        go_login()
      }
    })
  } else {
    ElMessage({
      type: 'error',
      message: '手机号或验证码或密码不能为空'
    })
  }
}

</script>

<style scoped>
.register {
  width: 100vw;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 10;
  background-color: rgba(0, 0, 0, 0.3);
}

.box {
  width: 400px;
  height: 480px;
  background-color: white;
  border-radius: 10px;
  position: relative;
  top: calc(50vh - 240px);
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
  margin-left: 90px;
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