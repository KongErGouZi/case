from utils.common_logger import logger
from rest_framework.viewsets import GenericViewSet
from .models import Banner
from utils.common_views import CommonCacheListModelMixin
from .serializer import BannerSerializer
from rest_framework.serializers import Serializer
from typing import Type
from django.db.models import QuerySet


# 首页轮播图接口
class BannerView(GenericViewSet, CommonCacheListModelMixin):
    """
    >>> {
    >>>"code": 200,
    >>>"msg": "请求成功",
    >>>"result": []
    >>>}
    """
    cache_key: str = 'banner_cache'
    queryset: QuerySet[Banner] = Banner.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class: Type[Serializer] = BannerSerializer

    def get_queryset(self):
        return super().get_queryset()[:3]
