# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-27 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170926_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='文章分类'),
        ),
        migrations.AlterField(
            model_name='article',
            name='comment',
            field=models.BigIntegerField(default=0, verbose_name='评论数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_time',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='digest',
            field=models.TextField(blank=True, null=True, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.CharField(max_length=200, verbose_name='题图'),
        ),
        migrations.AlterField(
            model_name='article',
            name='view',
            field=models.BigIntegerField(default=0, verbose_name='阅读数量'),
        ),
    ]
