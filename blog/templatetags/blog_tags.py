# -*- coding:utf-8 -*-
'''simple_tag '''


from django import template
from django.db.models import Count
from ..models import Article, Category, Tag


register = template.Library()


@register.simple_tag
def total_posts():
    '''返回总数'''
    return Article.objects.count()


@register.simple_tag
def all_posts():
    """所有文章"""
    return Article.objects.all()


@register.simple_tag
def get_categories():
    """分类目录"""
    return Category.objects.annotate(
        num_articles=Count('article')).filter(num_articles__gt=0)


@register.simple_tag
def get_tags():
    """获取标签"""
    return Tag.objects.annotate(
        num_posts=Count('article')).filter(num_posts__gt=0)

"""
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    '''最新文章的渲染模板'''
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
"""