import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import {createPinia} from 'pinia'
import ElementPlus from 'element-plus'
// claude: 引入 Element Plus 样式，否则所有 el- 组件无样式导致页面布局混乱
import 'element-plus/dist/index.css'
import './assets/css/global.css'

// 图标库引入
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

// 创建vue实例，跟组件是App.vue
let app = createApp(App)
// vue状态管理实例
let pinia = createPinia()

// entries ：对象转数组
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    // 全局注册组件，项目中直接写标签，不用一个个导入了
    app.component(key, component)

}

app.use(router).use(pinia).use(ElementPlus).mount('#app')
