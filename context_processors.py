from django.contrib.sites.models import Site
from core.models import Settings
from django.conf import settings

def domain(request):
    domain = Site.objects.get_current().domain
    return {
        'DOMAIN': domain
    }

def title_and_tagline(request):
    site = Site.objects.get_current()
    try:
        s = Settings.objects.get(site=site)
        return {
            'SITE_TITLE': s.title,
            'SITE_TAGLINE': s.tagline
        }
    except:
        return {}


def disqus(request):
    return {
        'DISQUS_ID': settings.DISQUS_ID,
        'DISQUS_DEBUG': settings.DISQUS_DEBUG
    }

