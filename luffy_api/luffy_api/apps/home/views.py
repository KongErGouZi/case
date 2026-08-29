from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.common_logger import logger
from rest_framework.viewsets import GenericViewSet
from .models import Banner
from utils.common_views import CommonListModelMixin as ListModelMixin
from .serializer import BannerSerializer


# 首页轮播图接口
class BannerView(GenericViewSet, ListModelMixin):
    """
    >>> {
    >>>"code": 200,
    >>>"msg": "请求成功",
    >>>"result": []
    >>>}
    """
    queryset = Banner.objects.filter(is_delete=False, is_show=True).order_by('orders')[:3]
    serializer_class = BannerSerializer
