from rest_framework.views import exception_handler
from .common_logger import logger
from builtins import Exception
from typing import Dict, Any
from rest_framework.response import Response


def common_exception_handler(exc: Exception, context: Dict[str, Any]) -> Response:
    """
    全局异常处理
    :param exc: 异常实例
    :param context: 上下文字典
    :return:
    """
    request = context.get('request')
    view = context.get('view')

    user = request.user.username or '匿名用户'
    path = request.get_full_path()
    method = request.method

    # 统一日志记录
    logger.error(f'用户【{user}】，访问地址【{path}】，请求方式是【{method}】，访问视图类【{str(view)}】，错误是【{str(exc)}】')

    # 统一返回格式
    res = exception_handler(exc, context)
    res_dict = {'code': 999, 'msg': '系统错误，请联系系统管理员'}
    msg = '服务器异常，请稍后再试'
    if res:
        if isinstance(res.data, dict):
            msg = res.data.get('detail') or res.data
        elif isinstance(res.data, list):
            msg = res.data[0]
        res_dict['code'] = 000
        res_dict['msg'] = str(msg)
    else:
        res_dict['code'] = 111
        res_dict['msg'] = str(exc)

    return Response(res_dict)
