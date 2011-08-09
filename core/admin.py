from core.models import Settings
from django.contrib import admin
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin

class SettingsAdmin(admin.ModelAdmin): 
    class Media: 
        js = ('%s/tiny_mce/tiny_mce.js' % settings.STATIC_URL, '%s/filebrowser/js/TinyMCEAdmin.js' % settings.STATIC_URL,) 

admin.site.register(Settings, SettingsAdmin)

class FlatpageAdmin(FlatPageAdmin): 
    class Media: 
        js = ('%s/tiny_mce/tiny_mce.js' % settings.STATIC_URL, '%s/filebrowser/js/TinyMCEAdmin.js' % settings.STATIC_URL,) 

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatpageAdmin)

