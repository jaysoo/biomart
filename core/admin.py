from core.models import Settings
from django.contrib import admin

class SettingsAdmin(admin.ModelAdmin): 
    class Media: 
        js = ('/static/tiny_mce/tiny_mce.js', '/static/filebrowser/js/TinyMCEAdmin.js',) 

admin.site.register(Settings, SettingsAdmin)
