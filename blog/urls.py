# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls.py 
   Description : blog urls
   Author :       cgDeepLearn
   date：          2017/4/13
-------------------------------------------------
   Change Activity:
                   2017/4/13:
-------------------------------------------------
"""


from blog import views
from django.conf.urls import url

app_name = 'blog'
urlpatterns = [
    url(r'^index/$', views.Index, name='index'),
    url(r'^about/$', views.About, name='about'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^link/$', views.Link, name='link'),
    url(r'^message$', views.Message, name='message'),
    url(r'^article/(?P<cate>[-\w]+)/$', views.Articles, name='article'),
    url(r'^get_comment/$', views.GetComment, name='get_comment'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),   
    url(r'^tag/(?P<name>.*?)/$', views.tag, name='tag'),
    url(r'archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archive_month, name='archive_month'),

]
