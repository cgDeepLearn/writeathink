# -*- coding: utf-8 -*
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')

app = Celery('django_blog')

# 这里定义了namespace='CELERY'，在settings里所有跟celery有关的设置都有加上'CELERY_'前缀
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# 自动搜索所有注册的app下的tasks.py，所有celery处理的任务，都写在app下的tasks.py里

app.autodiscover_tasks()

@app.task(bind=True)
def test_task(self):
    print('Request: {0!r}'.format(self.request))
