import axios from "../http";

export const requestLogin = (username, password) => axios.post('home/banner', {username, password})
export const reqCheckMobile = (mobile) => axios.get(`user/mobile/check_mobile/?mobile=${mobile}`)
export const reqSendSms = (mobile) => axios.post(`user/user/send_sms`, {mobile})
export const reqSmsLogin = (mobile, code) => axios.post(`user/user/sms_login`, {mobile, code})