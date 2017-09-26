# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     models.py
   Description :
   Author :       cgDeepLearn
   date：          2016/11/18
-------------------------------------------------
   Change Activity:
                   2016/11/18:
-------------------------------------------------
"""

from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(u'标签名', max_length=30)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(max_length=200)  # 博客标题
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', verbose_name='文章分类', on_delete=models.CASCADE)
    date_time = models.DateField(default=timezone.now, verbose_name='创建时间')  # 博客日期
    content = models.TextField(blank=True, null=True, verbose_name='正文')  # 文章正文
    digest = models.TextField(blank=True, null=True, verbose_name='摘要')  # 文章摘要
    picture = models.CharField(max_length=200, verbose_name='题图')  # 标题图片地址
    view = models.BigIntegerField(default=0, verbose_name='阅读数量')  # 阅读数
    comment = models.BigIntegerField(default=0, verbose_name='评论数')  # 评论数
    
    tag = models.ManyToManyField(Tag)  # 标签

    def __str__(self):
        return self.title

    def sourceUrl(self):
        source_url = settings.HOST + '/blog/detail/{id}'.format(id=self.pk)
        return source_url  # 给网易云跟帖使用

    def viewed(self):
        """
        增加阅读数
        :return:
        """
        self.view += 1
        self.save(update_fields=['view'])

    def commenced(self):
        """
        增加评论数
        :return:
        """
        self.comment += 1
        self.save(update_fields=['comment'])

    class Meta:  # 按时间降序
        ordering = ['-date_time']
        verbose_name = u"文章"
        verbose_name_plural = verbose_name


class Category(models.Model):
    name = models.CharField(u'分类名称', max_length=30)
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = u"分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(u"标题", max_length=100)
    source_id = models.CharField(u'文章id或source名称', max_length=25)
    create_time = models.DateTimeField(u'评论时间', auto_now=True)
    user_name = models.CharField(u'评论用户', max_length=25)
    url = models.CharField(u'链接', max_length=100)
    comment = models.CharField(u'评论内容', max_length=500)