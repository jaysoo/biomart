from models import Article
from django.contrib import admin
from django.conf import settings

def make_published(modeladmin, request, queryset):
    queryset.update(status=2)
make_published.short_description = "Mark selected stories as published"

class ArticleAdmin(admin.ModelAdmin): 
    list_display = ('title', 'author', 'pub_date', 'status')
    list_filter   = ('pub_date', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'pub_date'
    actions = [make_published]

    class Media: 
        js = ('%s/tiny_mce/tiny_mce.js' % settings.STATIC_URL, '%s/js/TinyMCEAdmin.js' % settings.STATIC_URL,) 

admin.site.register(Article, ArticleAdmin)

