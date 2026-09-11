import axios from "../http";

export const requestBanner = () => axios.get('home/banner')
export const reqSeckill = (courseId) => axios.post('home/seckill/seckill', {courseId})
export const reqResult = (taskId) => axios.post('home/seckill/result', {taskId})