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
              @blur="check_mobile">
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
              <span class="sms" @click="send_sms">{{ sms_interval }}</span>
            </template>
          </el-input>
          <el-button type="primary">注册</el-button>
        </el-form>
        <div class="foot">
          <span @click="go_login">立即登录</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

let $emit = defineEmits(['close', 'go'])

const close_register = () => {
  $emit('close')
}

const go_login = () => {
  $emit('go')
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