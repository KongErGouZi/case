from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BannerView, SeckillView

router = SimpleRouter()
router.register('banner', BannerView, 'banner')
router.register('seckill', SeckillView, 'seckill')

urlpatterns = [
]

urlpatterns += router.urls
