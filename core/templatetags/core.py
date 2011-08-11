from django import template
from django.db import models

import re

Navigation = models.get_model('core', 'navigation')

register = template.Library()

class GetNavigation(template.Node):
    def __init__(self, name, var_name):
        self.name = name
        self.var_name = var_name

    def render(self, context):
        if not self.name:
            self.name = 'top'
        navigation = Navigation.objects.filter(name=self.name)[0]
        context[self.var_name] = navigation
        return ''

@register.tag
def get_navigation(parser, token):
    """
    Gets any number of latest articles and stores them in a varable.

    Syntax::

        {% get_navigation [name] as [var_name] %}

    Example usage::

        {% get_navigation 'top' as navigation %}
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    format_string, var_name = m.groups()
    return GetNavigation(format_string, var_name)


