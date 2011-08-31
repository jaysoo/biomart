from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache
from utils import create_cache_key

class Settings(models.Model):
    site = models.ForeignKey(Site)
    title = models.CharField(_('site title'), max_length=100, default='BioMart')
    tagline = models.CharField(_('tagline'), max_length=100)
    project_overview = models.TextField()

    @staticmethod
    def get_current():
        site = Site.objects.get_current()
        key = create_cache_key(Settings, field='site__id', field_value=site.id)
        settings = cache.get(key, None)

        if not settings:
            try:
                settings = Settings.objects.get(site=site)
                cache.add(key, settings)
            except Navigation.DoesNotExist:
                return None

        return settings

    def __unicode__(self):
        return 'Settings for %s' % self.site.name

    class Meta:
        verbose_name_plural = _('settings')

class Navigation(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.CharField(_('description'), max_length=255)

    def get_items(self):
        return self.navitem_set.all().order_by('display_order')

    @staticmethod
    def get_navigation(name):
        key = create_cache_key(Navigation, field='name', field_value=name)
        navigation = cache.get(key, None)

        if not navigation:
            try:
                navigation = Navigation.objects.filter(name=name)[0]
                cache.add(key, navigation)
            except Navigation.DoesNotExist:
                return None

        return navigation

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'navigation'

class NavItem(models.Model):
    navigation = models.ForeignKey(Navigation)
    label = models.CharField(_('label'), max_length=100)
    url = models.CharField(_('URL'), max_length=100)
    display_order = models.IntegerField(help_text=_('Order that items will be displayed'))

class ThirdPartySoftware(models.Model):
    name = models.CharField(_('name'), max_length=100)
    url = models.URLField(_('URL'), max_length=100)

    @staticmethod
    def get_all():
        key = create_cache_key(ThirdPartySoftware, field='type', field_value='all')
        software_list = cache.get(key, None)

        if not software_list:
            try:
                software_list = ThirdPartySoftware.objects.all().order_by('name')
                cache.add(key, software_list)
            except Navigation.DoesNotExist:
                return None

        return software_list

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'third party software'

