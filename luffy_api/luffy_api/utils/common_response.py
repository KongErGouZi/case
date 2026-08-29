from __future__ import annotations
from rest_framework.response import Response
from typing import Dict, Any, Optional, List


class APIResponse(Response):

    def __init__(
            self,
            code: int = 100,
            msg: str = '请求成功',
            status: int = 200,
            headers: Optional[Dict[str, Any]] = None,
            **kwargs: Any
    ):
        """

        :param code:
        :param msg:
        :param status:
        :param headers:
        :param kwargs:
            username
            token
        """
        data = {
            'code': code,
            'msg': msg
        }
        if kwargs:
            data.update(kwargs)
        super().__init__(data=data, status=status, headers=headers)
