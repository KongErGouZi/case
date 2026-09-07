from .celery import app
from apps.home.models import Banner
from django.db.models import QuerySet
from apps.home.serializer import BannerSerializer
from django.conf import settings
from django.core.cache import cache


@app.task
def update_banner() -> bool:
    instance: QuerySet[Banner] = Banner.objects.all().filter(is_show=True, is_delete=False).order_by('orders')[:3]

    serializer = BannerSerializer(instance=instance, many=True)

    for item in serializer.data:
        item['image'] = settings.BACKEND_URL + item['image']

    cache.set('banner_cache', serializer.data)

    return True
