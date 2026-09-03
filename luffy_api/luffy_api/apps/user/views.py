from .models import User
from rest_framework.viewsets import ViewSet, GenericViewSet
from luffy_api.utils.common_response import APIResponse
from rest_framework.exceptions import APIException
from luffy_api.utils.common_logger import logger
from rest_framework.decorators import action
from .serializer import MulLoginSerializer
from luffy_api.libs.tx_sms import generate_code, send_sms_core
from django.core.cache import cache


# 不需要序列化，所有用ViewSet
class UserMobileView(ViewSet):
    # 手机号校验接口

    @action(methods=['get'], detail=False)
    def check_mobile(self, request, *args, **kwargs) -> APIResponse:
        mobile = request.query_params.get('mobile')
        if not mobile:
            return APIResponse(code=101, msg='请求参数不能为空')

        try:
            is_exist = User.objects.filter(mobile=mobile).exists()
            if not is_exist:
                logger.info(f'手机号校验失败：{mobile}')
                return APIResponse(code=101, msg='手机号不存在')
            logger.info(f'手机号校验成功：{mobile}')
            return APIResponse(msg='手机号存在')
        except Exception as e:
            logger.error(f'手机号校验接口异常：{e}', exc_info=True)
            raise APIException('校验异常')


class UserView(GenericViewSet):
    serializer_class = MulLoginSerializer

    @action(methods=['POST'], detail=False)
    def mul_login(self, request, *args, **kwargs) -> APIResponse:
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        username = serializer.context.get('username')
        token = serializer.context.get('token')
        icon = serializer.context.get('icon')

        return APIResponse(username=username, token=token, icon=icon)

    @action(methods=['POST'], detail=False)
    def send_sms(self, request, *args, **kwargs) -> APIResponse:
        """ 发送短信 """
        mobile = request.data.get('mobile')
        if not mobile:
            raise APIException(detail='手机号不能为空')

        code = generate_code()
        res = send_sms_core(mobile, code)

        if not res:
            raise APIException('短信发送失败')

        cache.set('SMS_CODE_%s' % mobile, code)
        return APIResponse(result=res, msg='短信发送成功')
