import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import {createPinia} from 'pinia'
import ElementPlus from 'element-plus'
// claude: 引入 Element Plus 样式，否则所有 el- 组件无样式导致页面布局混乱
import 'element-plus/dist/index.css'
import './assets/css/global.css'


let pinia = createPinia()
createApp(App).use(router).use(pinia).use(ElementPlus).mount('#app')
