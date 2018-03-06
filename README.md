## Django搭建博客
  [![](https://img.shields.io/badge/Django-1.11-green.svg)](http://www.writeathink.cn/blog/)
[![](https://img.shields.io/badge/Powered%20by-@cgDeepLearn-blue.svg)](http://www.writeathink.cn/blog/)

使用Django快速搭建博客
### 要求
* Python: 3.X
* Django: 1.10.x, 1.11.X
* Postgresql

### 示例博客：<http://www.writeathink.cn/blog>

### 特点

* 博客文章 markdown 渲染，代码高亮
* 三方社会化评论系统支持(畅言)
* 三种皮肤自由切换
* 阅读排行榜/最新评论
* 多目标源博文分享
* 博文归档
* 友情链接

### 下载
```
wget https://github.com/cgDeepLearn/django-blog/archive/master.zip
or
git clone git@github.com:cgDeepLearn/django-blog.git
```

### 安装

```shell
pip install -r requirements.txt  #安装所有依赖
setting.py配置自己的数据库
```

# 保密起见创建.env文件配置数据库

```conf
[postgresql]
db_name = ***
user = ***
pass = ***
port = 5432
[redis]
pass =
```

```
配置畅言：到http://changyan.kuaizhan.com/注册站点,将templates/message.html中js部分换成你在畅言中生成的js。
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
```

浏览器中打开<http://127.0.0.1:8000/>即可访问

## 历史版本变动

* change log
  * start    ---2017-3-25
  * add model view url    ---2017-4-3
  * add category, tag  ---2017-4-10
  * add html css ---2017-4-17
  * add js  ---2017-5-3
  * add comment, sitemap  ---2017-5-15
  * add blogtags  ---2017-5-20
  * add widget  ---2017-6-2
  * add host and depoly  ---2017-8-20
  * fix index  ---2017-8-22
  * fix search with whoosh, haystack ---2017-9-10
  * add archive, comment jump ---2017-10-17
  * add celery-redis  ---2018
  * add https  ---2018-3-5

* need to be done
  * (rank, url-slug, recommend, article picture change)
  * ( right html change with block(specially in detail), body with richtexteditor)
  * (homepage with top list, redis, celery)
  * (add recommend button)
  * (use cookiecutter)

