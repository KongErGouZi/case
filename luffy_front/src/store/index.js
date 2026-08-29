import {defineStore} from 'pinia'
export const definedLuffy = defineStore(
    'definedLuffy', //必须唯一
    {
        state: () => { // state中用于定义数据
            return {
                title:'luffy学城'

            }
        },
        getters: {
        },
        actions: {
        }
    }
)
