from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Settings(models.Model):
    site = models.ForeignKey(Site)
    title = models.CharField(_('site title'), max_length=100, default='BioMart')
    tagline = models.CharField(_('tagline'), max_length=100)
    project_overview = models.TextField()

    def __unicode__(self):
        return 'Settings for %s' % self.site.name

    class Meta:
        verbose_name_plural = _('settings')

class Navigation(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.CharField(_('description'), max_length=255)

    def get_items(self):
        return self.navitem_set.all().order_by('display_order')

    def __unicode__(self):
        return self.name

class NavItem(models.Model):
    navigation = models.ForeignKey(Navigation)
    label = models.CharField(_('label'), max_length=100)
    url = models.CharField(_('url'), max_length=100)
    display_order = models.IntegerField(help_text=_('Order that items will be displayed'))
