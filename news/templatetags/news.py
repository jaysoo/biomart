from django import template
from django.db import models

import re

Article = models.get_model('news', 'article')

register = template.Library()
class LatestArticles(template.Node):
    def __init__(self, limit, var_name):
        self.limit = int(limit)
        self.var_name = var_name

    def render(self, context):
        articles = Article.get_latest(self.limit)
        if articles and (self.limit == 1):
            context[self.var_name] = articles[0]
        else:
            context[self.var_name] = articles
        return ''

@register.tag
def get_latest_articles(parser, token):
    """
    Gets any number of latest articles and stores them in a varable.

    Syntax::

        {% get_latest_articles [limit] as [var_name] %}

    Example usage::

        {% get_latest_articles 10 as latest_article_list %}
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    format_string, var_name = m.groups()
    return LatestArticles(format_string, var_name)

class ArticleMonths(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        months = Article.objects.dates('pub_date', 'month').order_by('-pub_date')
        context[self.var_name] = months
        return ''

@register.tag
def get_months(parser, token):
    """
    Syntax::

        {% get_months as [var_name] %}

    Example usage::

        {% get_months as months %}
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    var_name = m.groups()[0]
    return ArticleMonths(var_name)

