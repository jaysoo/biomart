from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Settings(models.Model):
    site = models.ForeignKey(Site)
    title = models.CharField(_('site title'), max_length=100, default='BioMart')
    tagline = models.CharField(_('tagline'), max_length=100)
    project_overview = models.TextField()

    def __unicode__(self):
        return 'Settings for %s' % self.site.name

    class Meta:
        verbose_name_plural = _('settings')

