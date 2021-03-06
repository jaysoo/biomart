from core.models import Settings, Navigation, NavItem, ThirdPartySoftware
from django.contrib import admin
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django import forms
import time

class NavItemInlineForm(forms.ModelForm):
    class Meta:
        model = NavItem
    
class NavItemInline(admin.TabularInline):
    model = NavItem
    form = NavItemInlineForm
    ordering = ('display_order', 'label')

class NavigationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = (NavItemInline,)

admin.site.register(Navigation, NavigationAdmin)

class ThirdPartySoftwareAdmin(admin.ModelAdmin): 
    list_display = ('name', 'url')
    ordering = ('name', 'url')

admin.site.register(ThirdPartySoftware, ThirdPartySoftwareAdmin)

class SettingsAdmin(admin.ModelAdmin): 
    class Media: 
        js = (
            '%s/tiny_mce/tiny_mce.js' % settings.STATIC_URL,
            '%s/js/TinyMCEAdmin.js?d=%s' % ( settings.STATIC_URL, int(time.time() * 1000) ),
        )


admin.site.register(Settings, SettingsAdmin)

class FlatpageAdmin(FlatPageAdmin): 
    class Media:
        js = (
            '%s/tiny_mce/tiny_mce.js' % settings.STATIC_URL,
            '%s/js/TinyMCEAdmin.js?d=%s' % ( settings.STATIC_URL, int(time.time() * 1000) ),
        )


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatpageAdmin)

