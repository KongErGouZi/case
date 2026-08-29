from django.db import models
from utils.common_model import BaseModel


class Banner(BaseModel):
    title = models.CharField(max_length=16, unique=True, verbose_name='名称')
    image = models.ImageField(upload_to='banner', verbose_name='图片')
    link = models.CharField(max_length=64, verbose_name='跳转链接')
    info = models.TextField(verbose_name='详情')

    def __str__(self):
        return self.title
