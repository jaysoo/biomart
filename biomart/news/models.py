from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import truncate_html_words
from django.utils.safestring import mark_safe
from django.db.models import permalink
from django.utils.html import strip_tags
                           
from django.core.cache import cache
from core.utils import create_cache_key

from managers import PublicManager

class Article(models.Model):
    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )

    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique_for_date='pub_date')
    author = models.ForeignKey(User)
    teaser = models.TextField(blank=True, help_text=_('Short teaser text for latest articles'))
    body = models.TextField()
    pub_date = models.DateTimeField()
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    objects = PublicManager()

    @permalink
    def get_absolute_url(self):
        return ('news_detail_month_numeric', None, {
            'year': self.pub_date.year,
            'month': self.pub_date.strftime('%m').lower(),
            'day': self.pub_date.day,
            'slug': self.slug
        })

    def _get_safe_body(self):
        return mark_safe(self.body)
    safe_body = property(_get_safe_body)

    def _get_blurb(self):
        text = self.teaser if self.teaser else strip_tags( truncate_html_words(self.body, 100) )
        return mark_safe( text )
    blurb = property(_get_blurb)

    @staticmethod
    def get_latest(limit=20):
        key = create_cache_key(Article, field='type', field_value='latest_%s' % limit)
        articles = cache.get(key, None)

        if not articles:
            try:
                articles = Article.objects.published().order_by('-pub_date')[:limit]
                cache.add(key, articles)
            except Article.DoesNotExist:
                return None

        return articles

    def __unicode__(self):
        return self.title

