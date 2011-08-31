from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.sites.models import Site
from core.models import Settings

def home(request):
    site = Site.objects.get_current()
    settings = Settings.objects.get(site=site)
    return render_to_response('home.html', {
        'project_overview': settings.project_overview,
    }, context_instance=RequestContext(request))
