from django.contrib import admin
from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'link', 'orders')
    # 增加自定义按钮
    actions = ['make_copy', ]

    def make_copy(self, request, queryset):
        print(queryset)
        print(request)

    # # 显示的文本，与django admin一致
    make_copy.short_description = '复制'
    # # icon，参考element-ui icon与https://fontawesome.com
    # make_copy.icon = 'fas fa-audio-description'
    #
    # # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    make_copy.type = 'danger'
    #
    # # 给按钮追加自定义的颜色
    # make_copy.style = 'color:black;'
