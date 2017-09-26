from django.contrib import admin

# Register your models here.


from blog.models import Tag, Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time'
    list_display = ('title', 'category', 'author', 'date_time', 'view')
    list_filter = ('category', 'author')
    search_fields = ('title', 'content')
    filter_horizontal = ('tag',)
    odering = ['date_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
