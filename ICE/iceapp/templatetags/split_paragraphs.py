from django import template
import re
register = template.Library()

@register.filter
def split_paragraphs(value):
    paragraphs = re.split(r'\n+', value)
    formatted_paragraphs = ''.join(f'<p>{p.strip()}</p>' for p in paragraphs if p.strip())
    return formatted_paragraphs