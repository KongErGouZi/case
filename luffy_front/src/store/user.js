import {defineStore} from 'pinia'
// 导入cookie
import $cookie from 'vue-cookies'

export const definedUser = defineStore('userPinia',
    {
        //必须唯一
        state: () => {
            return {
                login_user: {
                    username: $cookie.get('username'),
                    icon: $cookie.get('icon'),
                    token: $cookie.get('token')
                }
            }
        },
        actions: {
            set_user(user) {
                this.login_user = user
                // 存到cookie
                $cookie.set('token', user.token, '7d')
                $cookie.set('username', user.username, '7d')
                $cookie.set('icon', user.icon, '7d')
            },
            log_out() {
                this.login_user = {
                    username: '',
                    icon: '',
                    token: ''
                }
                $cookie.remove('username')
                $cookie.remove('icon')
                $cookie.remove('token')

            }
        }
    }
)