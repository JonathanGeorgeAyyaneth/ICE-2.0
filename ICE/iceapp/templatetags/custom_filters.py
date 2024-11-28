import re
from django.urls import reverse
from django import template
from iceapp.models import Person, InstitutionBuilding, ChurchAndOtherBuilding, MajorCelebrationHistoricalEvent, ChurchCommunity

register = template.Library()

@register.filter
def linkify_article(content):
    # Create dictionaries of names and their IDs
    person_names = {p.name.lower(): p.id for p in Person.objects.all()}
    institution_names = {i.name.lower(): i.id for i in InstitutionBuilding.objects.all()}
    building_names = {b.name.lower(): b.id for b in ChurchAndOtherBuilding.objects.all()}
    event_names = {e.name.lower(): e.id for e in MajorCelebrationHistoricalEvent.objects.all()}
    church_community_names = {c.name.lower(): c.id for c in ChurchCommunity.objects.all()}

    def replace_name_with_link(match):
        name = match.group(0)
        type = None
        
        # Case-insensitive lookup
        lower_name = name.lower()
        if lower_name in person_names:
            id = person_names[lower_name]
            type = 'person_detail'
        elif lower_name in institution_names:
            id = institution_names[lower_name]
            type = 'institution_building_detail'
        elif lower_name in building_names:
            id = building_names[lower_name]
            type = 'church_and_other_building_detail'
        elif lower_name in event_names:
            id = event_names[lower_name]
            type = 'major_celebration_historical_event_detail'
        elif lower_name in church_community_names:
            id = church_community_names[lower_name]
            type = 'church_community_detail'
        else:
            return name  # If the name is not found, return it as is

        url = reverse(type, args=[id])
        return f'<a href="{url}">{name}</a>'

    # Create regex patterns for case-insensitive matching
    patterns = {
        'person': re.compile('|'.join(map(re.escape, person_names.keys())), re.IGNORECASE),
        'institution_building': re.compile('|'.join(map(re.escape, institution_names.keys())), re.IGNORECASE),
        'church_and_other_building': re.compile('|'.join(map(re.escape, building_names.keys())), re.IGNORECASE),
        'major_celebration_historical_event': re.compile('|'.join(map(re.escape, event_names.keys())), re.IGNORECASE),
        'church_community': re.compile('|'.join(map(re.escape, church_community_names.keys())), re.IGNORECASE),
    }

    # Apply patterns to the content
    for key, pattern in patterns.items():
        content = pattern.sub(replace_name_with_link, content)

    return content
