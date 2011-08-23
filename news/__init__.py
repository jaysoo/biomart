from models import Article
from signals import invalidate_articles_cache
from django.db.models import signals

signals.post_save.connect(invalidate_articles_cache, Article, True)

