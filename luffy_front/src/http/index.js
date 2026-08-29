import axios from "axios";
import {ElMessage} from "element-plus";

const request = axios.create({
    baseURL: "http://127.0.0.1:8000/api/v1/",
    timeout: 5000,
    headers: {
        'Content-Type': "application/json; charset=utf-8"
    }
})

request.interceptors.request.use((config) => {
    let token = localStorage.getItem('token')
    if (token) {
        config.headers.token = 'banner' + token
    }
    return config
})

request.interceptors.response.use(response => {
        let res = response.data
        if (res.code === 100) {
            return response.data
        } else {
            ElMessage({
                type: 'Error',
                message: !res.message ? '请求服务器异常,请联系管理员' : res.message
            })
            return Promise.reject(response.data.message)
        }
    },
    error => {
        ElMessage({
            type: 'error',
            message: '服务器异常，请稍后再试'
        })
        return Promise.reject(new Error(error.message))
    })

export default request