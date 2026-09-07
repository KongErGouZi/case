from celery import Celery
import os
from datetime import timedelta

# 手动指定django配置文件，如果环境变量已经存在，则不覆盖
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffy_api.settings.dev')
broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'

app = Celery('mian',
             broker=broker,
             backend=backend,
             include=['celery_task.home_tasks', 'celery_task.user_task'])

# 指定时区，celery 默认UTC，启用定时任务时，需要修改时区
app.conf.timezone = 'Asia/Shanghai'
app.conf.enable_utc = False

app.conf.beat_schedule = {
    # 'send_sms': {
    #     'task': 'celery_task.home_task.send_sms',
    #     'schedule': timedelta(seconds=5),
    #     'args': (18956875441,),
    # },
    # 'add_age': {
    #     'task': 'celery_task.user_task.add_age',
    #     'schedule': crontab(hour=9, minute=16,day_of_week=3),  # 每周三早9点16
    #     'args': (44,55),
    # },

    'update_banner': {
        'task': 'celery_task.home_task.update_banner',
        'schedule': timedelta(seconds=10),
        'args': (),
    },
}
