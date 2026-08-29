// 导入路由创建的相关方法
import {createRouter,createWebHistory} from 'vue-router'

// 导入vue组件
import HomeView from '../views/HomeView.vue'

// 创建路由对象,声明路由规则
const router = createRouter({
    history: createWebHistory(),
    routes:[
        {
            path:'/',
            component:HomeView
        },
    ]

})

// 对外暴露路由对象
export default router;
