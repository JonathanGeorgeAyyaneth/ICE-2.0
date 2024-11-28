import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def link(text):
    """
    Convert URLs in the text into clickable links.
    """
    url_pattern = re.compile(r'(www\.[^\s]+)')
    text_with_links = url_pattern.sub(lambda match: f'<a href="http://{match.group(0)}" target="_blank">{match.group(0)}</a>', text)
    return mark_safe(text_with_links)
