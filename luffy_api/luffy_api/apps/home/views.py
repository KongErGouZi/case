from utils.common_logger import logger
from rest_framework.viewsets import GenericViewSet
from .models import Banner
from utils.common_views import CommonCacheListModelMixin
from .serializer import BannerSerializer
from rest_framework.serializers import Serializer
from typing import Type
from django.db.models import QuerySet
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from celery_task.home_task import seckill
from celery_task.celery import app
from utils.common_response import APIResponse
from celery.result import AsyncResult


# 首页轮播图接口
class BannerView(GenericViewSet, CommonCacheListModelMixin):
    cache_key: str = 'banner_cache'
    queryset: QuerySet[Banner] = Banner.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class: Type[Serializer] = BannerSerializer

    def get_queryset(self):
        return super().get_queryset()[:3]


class SeckillView(ViewSet):

    @action(methods=['POST'], detail=False)
    def seckill(self, request, *args, **kwargs):
        """ 提交任务，开启秒杀 """
        course_id = request.data.get('courseID')
        task_id = seckill.delay(course_id)
        return APIResponse(msg='排队中', task_id=str(task_id))

    @action(methods=['POST'], detail=False, url_path='result')
    def get_result(self, request, *args, **kwargs):
        """ 获取任务结构 """
        task_id = request.data.get('task_id')
        a = AsyncResult(id=task_id, app=app)
        if a.successful():
            res = a.get()
            if not res:
                return APIResponse(success='0', msg='秒杀失败')
            return APIResponse(success='1', msg='秒杀成功')
        elif a.status == 'PENDING':
            return APIResponse(msg='查询中...')
        else:
            return APIResponse(msg='查询中...')
