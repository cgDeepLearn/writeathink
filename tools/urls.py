# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls.py 
   Description : blog urls
   Author :       cgDeepLearn
   date：          2018/2/8
-------------------------------------------------
   Change Activity:
                   2018/2/8: add tools
-------------------------------------------------
"""


from tools import views
from django.conf.urls import url

app_name = 'tools'
urlpatterns = [
    url(r'^test/$', views.test_hello, name='test')
]