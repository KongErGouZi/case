from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserMobileView, UserView

router = SimpleRouter()
router.register('mobile', UserMobileView, 'mobile')
router.register('user', UserView, 'user')

urlpatterns = []

urlpatterns += router.urls
