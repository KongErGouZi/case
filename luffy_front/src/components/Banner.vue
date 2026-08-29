<template>
  <div class="banner">
    <el-carousel height="400px" :interval="5000" arrow="always">
      <el-carousel-item v-for="item in banner_list" :key="item">
        <img :src="item.image" alt="">
      </el-carousel-item>

    </el-carousel>
  </div>
</template>

<script setup>
import axios from '../http'
import {ref, reactive} from 'vue'

const banner_list = reactive({})

axios.get('home/banner').then(res => {
  Object.assign(banner_list, res.result)
  console.log(banner_list)
})

</script>

<style scoped>
/* claude: 轮播图恢复全宽铺满，不做固定宽度限制 */
/* claude: 去掉写死的 min-width:1200px，避免窗口较小时轮播溢出，改用 width:100% 自适应 */
.el-carousel__item {
  height: 400px;
  width: 100%;
}

.el-carousel__item img {
  height: 400px;
  width: 100%;
  /* claude: 保持图片原始比例并裁剪填充，避免超宽 banner 图被垂直拉伸变形 */
  object-fit: cover;
}
</style>