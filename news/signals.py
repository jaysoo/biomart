from django.core.cache import cache
from models import Article
from core.utils import create_cache_key

def invalidate_articles_cache(sender=None, instance=None, isnew=False, **kwargs):
    # Clear published articles cache
    key1 = create_cache_key(Article, field='type', field_value='published')
    cache.set(key1, None, 5)

    if isnew:
        return

    key2 = create_cache_key(Article, field='id', field_value=instance.id)
    cache.set(key2, None, 5)


