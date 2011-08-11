from django.contrib.sites.models import Site
from core.models import Settings

def domain(request):
    domain = Site.objects.get_current().domain
    return {
        'DOMAIN': domain
    }

def title_and_tagline(request):
    site = Site.objects.get_current()
    try:
        settings = Settings.objects.get(site=site)
        return {
            'SITE_TITLE': settings.title,
            'SITE_TAGLINE': settings.tagline
        }
    except:
        return {}


