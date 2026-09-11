<template>
  <div>
    <Header></Header>
    <div style="padding: 50px;margin-left: 100px">


      <h1>Go语言课程</h1>
      <img src="../assets/img/changchui001.png"
           height="300px"
           width="300px">
      <br>
      <el-button type="danger" @click="handleSeckill" v-loading.fullscreen.lock="fullscreenLoading">秒杀课程</el-button>
    </div>


    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>


    <Footer></Footer>

  </div>
</template>

<script setup>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import {ElMessage} from "element-plus";
import {ref} from 'vue'
import {reqSeckill, reqResult} from "../api/home.js";


const fullscreenLoading = ref(false)
const courseId = '99'

async function handleSeckill() {
  fullscreenLoading.value = true
  let res = await reqSeckill(courseId)
  let taskId = res.data.get('task_id')

  let t = null
  t = setInterval(async () => {
    let taskResult = await reqResult(taskId)
    if (taskResult.data.success === '1' || taskResult.data.success === '0') {
      fullscreenLoading.value = false
      clearInterval(t)
      t = null
      ElMessage({
        type: 'success',
        message: taskResult.data.msg
      })
    } else {
      ElMessage({
        type: 'success',
        message: taskResult.data.msg
      })
    }
  }, 1000)

}


</script>

<style scoped>

</style>