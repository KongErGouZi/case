from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BannerView

router = SimpleRouter()
router.register('banner', BannerView, 'banner')

urlpatterns = [
]

urlpatterns += router.urls
