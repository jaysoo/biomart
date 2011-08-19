from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from models import Article


class ArticlesFeed(Feed):
    _site = Site.objects.get_current()
    title = '%s feed' % _site.name
    description = '%s news feed.' % _site.name

    def link(self):
        return reverse('news_index')

    def items(self):
        return Article.objects.published()[:20]

    def item_pubdate(self, obj):
        return obj.pub_date
