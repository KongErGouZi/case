from .celery import app
from home.models import Banner
from home.serializer import BannerSerializer
from django.db.models import QuerySet

from django.conf import settings
from django.core.cache import cache
import time
import random


@app.task
def update_banner() -> bool:
    """ 定时更新轮播图 """

    instance: QuerySet[Banner] = Banner.objects.all().filter(is_show=True, is_delete=False).order_by('orders')[:3]

    serializer = BannerSerializer(instance=instance, many=True)

    for item in serializer.data:
        item['image'] = settings.BACKEND_URL + item['image']

    cache.set('banner_cache', serializer.data)

    return True


@app.task
def seckill(course_id):
    # 根据课程id去数据库查询结果
    time.sleep(1)
    res = random.choice([False, True])
    time.sleep(1)
    if res:
        # 库存减一
        # 下单
        return True
    else:
        return False
