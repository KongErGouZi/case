from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from .common_response import APIResponse
from typing import Optional
from django.core.cache import cache


class CommonListModelMixin(ListModelMixin):

    def list(self, request, *args, **kwargs) -> APIResponse:
        result = super().list(request, *args, **kwargs)

        return APIResponse(result=result.data)


class CommonCacheListModelMixin(ListModelMixin):
    """ 缓存处理 """
    cache_key: str = ''

    def list(self, request, *args, **kwargs) -> APIResponse:
        if not self.cache_key:
            raise AttributeError("cache_key 未设置")

        res = cache.get(self.cache_key, None)

        if res is None:
            res = super().list(request, *args, **kwargs)
            cache.set(self.cache_key, res.data)
            return APIResponse(result=res.data)
        return APIResponse(result=res)
