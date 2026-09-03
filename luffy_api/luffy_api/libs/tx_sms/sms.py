from __future__ import annotations
import json
import random
from .settings import *
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.sms.v20210111 import sms_client, models
# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from utils.common_logger import logger


def generate_code(num: int | str = 4) -> str:
    """ 验证码生成 """
    code = ''
    for _ in range(int(num)):
        code += str(random.randint(0, 9))
    return code


def send_sms_core(mobile: str, code: str) -> bool:
    """ 发送短信 """
    try:
        cred = credential.Credential(SECRET_ID, SECRET_KEY)
        httpProfile = HttpProfile()
        httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
        httpProfile.reqTimeout = 10  # 请求超时时间，单位为秒(默认60秒)
        httpProfile.endpoint = "sms.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)
        clientProfile = ClientProfile()
        clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法
        clientProfile.language = "en-US"
        clientProfile.httpProfile = httpProfile
        client = sms_client.SmsClient(cred, "ap-guangzhou", clientProfile)
        req = models.SendSmsRequest()
        req.SmsSdkAppId = SMS_SDK_APPID
        req.SignName = SIGN_NAME
        # 模板 ID: 必须填写已审核通过的模板 ID
        # 模板 ID 可前往 [国内短信](https://console.cloud.tencent.com/smsv2/csms-template) 或 [国际/港澳台短信](https://console.cloud.tencent.com/smsv2/isms-template) 的正文模板管理查看
        req.TemplateId = TEMPLATE_ID
        # 模板参数: 模板参数的个数需要与 TemplateId 对应模板的变量个数保持一致，，若无模板参数，则设置为空
        req.TemplateParamSet = [code, LEFT_TIME]
        # 下发手机号码，采用 E.164 标准，+[国家或地区码][手机号]
        # 示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号
        req.PhoneNumberSet = ["+86" + mobile]
        # 用户的 session 内容（无需要可忽略）: 可以携带用户侧 ID 等上下文信息，server 会原样返回
        req.SessionContext = ""
        req.ExtendCode = ""
        req.SenderId = ""
        resp = client.SendSms(req)
        # print(resp.to_json_string(indent=2))
        # 输出json格式的字符串回包
        res = json.loads(resp.to_json_string(indent=2))
        # res = resp.to_json_string(indent=2)
        # print(res)
        if res.get('SendStatusSet')[0].get('Code') == 'Ok':
            return True
        else:
            logger.warning(res.get('SendStatusSet')[0].get('Message'))
            return False
    except TencentCloudSDKException as err:
        logger.error(err)
        # 应该记录日志
        return False


if __name__ == '__main__':
    print(generate_code(5))
