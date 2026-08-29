<template>
  <Header></Header>
  <Banner></Banner>
  <!-- claude: 栅格间距改用 el-row 的 gutter 控制，不再给 el-col 加 padding -->
  <div class="course">
    <el-row :gutter="20">
      <el-col :span="6" v-for="(o, index) in 8" :key="o">
        <el-card :body-style="{ padding: '0px' }" class="course_card">
          <img src="../assets/img/changchui001.png"
               class="image">
          <div style="padding: 14px;">
            <span class="course_title">推荐课程</span>
            <div class="bottom clearfix">
              <time class="time">价格：999</time>
              <el-button type="text" class="button">查看详情</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
  <!-- claude: 原 16:9 大图被强制 500px 高度会压扁变形，改用 object-fit:cover 保持比例裁剪 -->
  <div class="promo">
    <img src="../assets/img/zhangchui002.png" alt="">
  </div>
  <Footer></Footer>
</template>

<script setup lang="js">
import Header from '../components/Header.vue'
import Banner from '../components/Banner.vue'
import Footer from '../components/Footer.vue'
</script>

<style scoped>
.time {
  /* claude: 价格字号调大到 16px */
  font-size: 16px;
  color: #999;
}

/* claude: 卡片标题「推荐课程」字号调大到 20px 并加粗，更醒目 */
.course_title {
  font-size: 20px;
  font-weight: bold;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  /* claude: 固定 16:9 比例，让 8 张卡片图片高度统一整齐 */
  aspect-ratio: 16 / 9;
  /* claude: 保持比例裁剪，避免图片被拉伸变形 */
  object-fit: cover;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both
}

/* claude: 课程区域统一留白，卡片横向间距由 el-row 的 gutter 控制 */
.course {
  /* claude: 课程区恢复全宽铺满窗口 */
  padding: 20px;
}

/* claude: 卡片纵向间距，替代原先给 el-col 加的 50px padding */
.course_card {
  margin-bottom: 20px;
}

/* claude: 底部宣传大图，固定高度 + object-fit:cover，保持 16:9 比例不被拉伸变形 */
.promo img {
  width: 100%;
  height: 400px;
  object-fit: cover;
  display: block;
}
</style>