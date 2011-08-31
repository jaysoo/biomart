import re
import hashlib

from django.db.models.manager import Manager
from django.utils.encoding import smart_str

def clean_cache_key(key):

    #logic below borrowed from http://richwklein.com/2009/08/04/improving-django-cache-part-ii/ 
    cache_key = re.sub(r'\s+', '-', key)
    cache_key = smart_str(cache_key)

    if len(cache_key) > 250:
         cache_key = cache_key[:200] + '-' + hashlib.md5(cache_key).hexdigest()

    return cache_key
        
def create_cache_key(klass, field=None, field_value=None):
    key_model = "%s.%s.%s:%s"
    key = ''

    if field and field_value:
        if isinstance(klass, Manager):
            key = key_model % (klass.model._meta.app_label, klass.model._meta.module_name, field, field_value)
        else:
            key = key_model % (klass._meta.app_label, klass._meta.module_name, field, field_value)

    if key is '':
        raise Exception('Cache key cannot be empty.')

    return clean_cache_key(key)
