from django.core.cache import cache
from models import Settings, Navigation, ThirdPartySoftware
from utils import create_cache_key

def invalidate_settings_cache(sender=None, instance=None, isnew=False, **kwargs):
    if isnew:
        return

    site_id = instance.site.id
    key = create_cache_key(Settings, field='site__id', field_value=site_id)
    cache.set(key, None, 5)

def invalidate_navigation_cache(sender=None, instance=None, isnew=False, **kwargs):
    if isnew:
        return

    key = create_cache_key(Navigation, field='name', field_value=instance.name)
    cache.set(key, None, 5)

def invalidate_thirdpartysoftware_cache(sender=None, instance=None, isnew=False, **kwargs):
    if isnew:
        return

    key = create_cache_key(ThirdPartySoftware, field='type', field_value='all')
    cache.set(key, None, 5)

