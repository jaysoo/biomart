from django.core.cache import cache
from models import Article
from core.utils import create_cache_key

def invalidate_articles_cache(sender=None, instance=None, isnew=False, **kwargs):
    if isnew:
        return
    key = create_cache_key(Article, field='id', field_value=instance.id)
    cache.set(key, None, 5)


