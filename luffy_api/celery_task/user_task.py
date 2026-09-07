from .celery import app
from luffy_api import logger
from luffy_api.libs.tx_sms import send_sms_core


@app.task
def send_sms_celery(mobile, code):
    logger.info('向%s发送短信' % mobile)
    res = send_sms_core(mobile, code)
    return res
