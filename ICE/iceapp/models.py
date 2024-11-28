from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .translation_utils import translate_text


class ChurchCommunity(models.Model):

    selection = [ ('Communities','Communities'),
                  ('Diocese','Diocese'),
                  ('Congregations','Congregations'),
                  ('Pios Associations','Pios Associations'),
                  ]

    name = models.CharField(max_length=255)
    category= models.CharField(max_length=50, choices=selection)
    about = models.TextField(blank=True, null=True)
    about_ml = models.TextField(blank=True, null=True)
    about_hi=models.TextField(blank=True,null=True)
    about_image = models.ImageField(upload_to='church_community/', blank=True, null=True)
    
    governance_and_structure = models.TextField(blank=True, null=True)
    governance_and_structure_ml = models.TextField(blank=True, null=True)
    governance_and_structure_hi = models.TextField(blank=True, null=True)
    governance_and_structure_image = models.ImageField(upload_to='church_community/', blank=True, null=True)
    
    worship_practices_and_rituals = models.TextField(blank=True, null=True)
    worship_practices_and_rituals_ml = models.TextField(blank=True, null=True)
    worship_practices_and_rituals_hi = models.TextField(blank=True, null=True)
    worship_practices_and_rituals_image = models.ImageField(upload_to='church_community/', blank=True, null=True)
    
    beliefs_and_teachings = models.TextField(blank=True, null=True)
    beliefs_and_teachings_ml = models.TextField(blank=True, null=True)
    beliefs_and_teachings_hi = models.TextField(blank=True, null=True)
    beliefs_and_teachings_image = models.ImageField(upload_to='church_community/', blank=True, null=True)
    
    community_life = models.TextField(blank=True, null=True)
    community_life_ml = models.TextField(blank=True, null=True)
    community_life_hi = models.TextField(blank=True, null=True)
    community_life_image = models.ImageField(upload_to='church_community/', blank=True, null=True)
    
    historical_figures = models.TextField(blank=True, null=True)
    historical_figures_ml = models.TextField(blank=True, null=True)
    historical_figures_hi = models.TextField(blank=True, null=True)
    historical_figures_image = models.ImageField(upload_to='church_community/', blank=True, null=True)
    
    conclusion = models.TextField(blank=True, null=True)
    conclusion_ml = models.TextField(blank=True, null=True)
    conclusion_hi = models.TextField(blank=True, null=True)
    conclusion_image = models.ImageField(upload_to='church_community/', blank=True, null=True)
    
    references = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=155)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='church_community_likes', blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='church_community_dislikes', blank=True)

    def __str__(self):
        return self.name

class Person(models.Model):

    selection = [ ('Clergy','Clergy'),
                  ('Laity','Laity'),
                  ('Saints','Saints'),
                  ('Eminent Persons','Eminent Persons'), ]
    
    name = models.CharField(max_length=255)
    category=models.CharField(max_length=50, choices=selection)
    about = models.TextField(blank=True, null=True)
    about_ml = models.TextField(blank=True, null=True)
    about_hi = models.TextField(blank=True, null=True)
    about_image = models.ImageField(upload_to='person/', blank=True, null=True)
    
    early_life = models.TextField(blank=True, null=True)
    early_life_ml = models.TextField(blank=True, null=True)
    early_life_hi = models.TextField(blank=True, null=True)
    early_life_image = models.ImageField(upload_to='person/', blank=True, null=True)
    
    key_achievements = models.TextField(blank=True, null=True)
    key_achievements_ml = models.TextField(blank=True, null=True)
    key_achievements_hi = models.TextField(blank=True, null=True)
    key_achievements_image = models.ImageField(upload_to='person/', blank=True, null=True)
    
    influence_and_legacy = models.TextField(blank=True, null=True)
    influence_and_legacy_ml = models.TextField(blank=True, null=True)
    influence_and_legacy_hi = models.TextField(blank=True, null=True)
    influence_and_legacy_image = models.ImageField(upload_to='person/', blank=True, null=True)
    
    veneration_recognition = models.TextField(blank=True, null=True)
    veneration_recognition_ml = models.TextField(blank=True, null=True)
    veneration_recognition_hi = models.TextField(blank=True, null=True)
    veneration_recognition_image = models.ImageField(upload_to='person/', blank=True, null=True)
    
    personal_reflections = models.TextField(blank=True, null=True)
    personal_reflections_ml = models.TextField(blank=True, null=True)
    personal_reflections_hi = models.TextField(blank=True, null=True)
    personal_reflections_image = models.ImageField(upload_to='person/', blank=True, null=True)
    
    conclusion = models.TextField(blank=True, null=True)
    conclusion_ml = models.TextField(blank=True, null=True)
    conclusion_hi = models.TextField(blank=True, null=True)
    conclusion_image = models.ImageField(upload_to='person/', blank=True, null=True)
    
    references = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=155)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='person_likes', blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='person_dislikes', blank=True)

    def __str__(self):
        return self.name

class InstitutionBuilding(models.Model):
    selection = [ ('Universities','Universities'),
                  ('Colleges','Colleges'),
                  ('Schools','Schools'),
                  ('Technical Institutions','Technical Institutions'),
                  ('Medical Colleges','Medical Colleges'),
                  ('Hospitals','Hospitals'),
                  ('Charity Institutions','Charity Institutions'),
                  ('Amenity Centres','Amenity Centres') ]

    name = models.CharField(max_length=255)
    category=models.CharField(max_length=50,choices=selection)
    about = models.TextField(blank=True, null=True)
    about_ml = models.TextField(blank=True, null=True)
    about_hi = models.TextField(blank=True, null=True)
    about_image = models.ImageField(upload_to='institution_building/', blank=True, null=True)
    
    history = models.TextField(blank=True, null=True)
    history_ml = models.TextField(blank=True, null=True)
    history_hi = models.TextField(blank=True, null=True)
    history_image = models.ImageField(upload_to='institution_building/', blank=True, null=True)
    
    mission_and_values = models.TextField(blank=True, null=True)
    mission_and_values_ml = models.TextField(blank=True, null=True)
    mission_and_values_hi = models.TextField(blank=True, null=True)
    mission_and_values_image = models.ImageField(upload_to='institution_building/', blank=True, null=True)
    
    services_and_programs = models.TextField(blank=True, null=True)
    services_and_programs_ml = models.TextField(blank=True, null=True)
    services_and_programs_hi = models.TextField(blank=True, null=True)
    services_and_programs_image = models.ImageField(upload_to='institution_building/', blank=True, null=True)
    
    impact_and_reach = models.TextField(blank=True, null=True)
    impact_and_reach_ml = models.TextField(blank=True, null=True)
    impact_and_reach_hi = models.TextField(blank=True, null=True)
    impact_and_reach_image = models.ImageField(upload_to='institution_building/', blank=True, null=True)
    
    governance_and_leadership = models.TextField(blank=True, null=True)
    governance_and_leadership_ml = models.TextField(blank=True, null=True)
    governance_and_leadership_hi = models.TextField(blank=True, null=True)
    governance_and_leadership_image = models.ImageField(upload_to='institution_building/', blank=True, null=True)
    
    notable_achievements = models.TextField(blank=True, null=True)
    notable_achievements_ml = models.TextField(blank=True, null=True)
    notable_achievements_hi = models.TextField(blank=True, null=True)
    notable_achievements_image = models.ImageField(upload_to='institution_building/', blank=True, null=True)
    
    conclusion = models.TextField(blank=True, null=True)
    conclusion_ml = models.TextField(blank=True, null=True)
    conclusion_hi = models.TextField(blank=True, null=True)
    conclusion_image = models.ImageField(upload_to='institution_building/', blank=True, null=True)
    
    references = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=155)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='institution_building_likes', blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='institution_building_dislikes', blank=True)

    def __str__(self):
        return self.name

class ChurchAndOtherBuilding(models.Model):
    selection = [ ('Basilica','Basilica'),
                  ('Cathedrals','Cathedrals'),
                  ('Parishes','Parishes'),
                  ('Pilgrime Centers','Pilgrime Centers'),]
    
    name = models.CharField(max_length=255)
    category=models.CharField(choices=selection, max_length=60)
    about = models.TextField(blank=True, null=True)
    about_ml = models.TextField(blank=True, null=True)
    about_hi = models.TextField(blank=True, null=True)
    about_image = models.ImageField(upload_to='church_and_other_building/', blank=True, null=True)
    
    history = models.TextField(blank=True, null=True)
    history_ml = models.TextField(blank=True, null=True)
    history_hi = models.TextField(blank=True, null=True)
    history_image = models.ImageField(upload_to='church_and_other_building/', blank=True, null=True)
    
    architecture_and_design = models.TextField(blank=True, null=True)
    architecture_and_design_ml = models.TextField(blank=True, null=True)
    architecture_and_design_hi = models.TextField(blank=True, null=True)
    architecture_and_design_image = models.ImageField(upload_to='church_and_other_building/', blank=True, null=True)
    
    functions_and_services = models.TextField(blank=True, null=True)
    functions_and_services_ml = models.TextField(blank=True, null=True)
    functions_and_services_hi = models.TextField(blank=True, null=True)
    functions_and_services_image = models.ImageField(upload_to='church_and_other_building/', blank=True, null=True)
    
    community_impact = models.TextField(blank=True, null=True)
    community_impact_ml = models.TextField(blank=True, null=True)
    community_impact_hi = models.TextField(blank=True, null=True)
    community_impact_image = models.ImageField(upload_to='church_and_other_building/', blank=True, null=True)
    
    governance_and_leadership = models.TextField(blank=True, null=True)
    governance_and_leadership_ml = models.TextField(blank=True, null=True)
    governance_and_leadership_hi = models.TextField(blank=True, null=True)
    governance_and_leadership_image = models.ImageField(upload_to='church_and_other_building/', blank=True, null=True)
    
    notable_features = models.TextField(blank=True, null=True)
    notable_features_ml = models.TextField(blank=True, null=True)
    notable_features_hi = models.TextField(blank=True, null=True)
    notable_features_image = models.ImageField(upload_to='church_and_other_building/', blank=True, null=True)
    
    conclusion = models.TextField(blank=True, null=True)
    conclusion_ml = models.TextField(blank=True, null=True)
    conclusion_hi = models.TextField(blank=True, null=True)
    conclusion_image = models.ImageField(upload_to='church_and_other_building/', blank=True, null=True)

    references = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=155)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='church_and_other_building_likes', blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='church_and_other_building_dislikes', blank=True)

    def __str__(self):
        return self.name

class MajorCelebrationHistoricalEvent(models.Model):

    selection = [ ('Historical Events','Historical Events'),
                  ('Major Celebrations','Major Celebrations'),]

    name = models.CharField(max_length=255)
    category=models.CharField(max_length=50, choices=selection)
    about = models.TextField(blank=True, null=True)
    about_ml=models.TextField(blank=True,null=True)
    about_hi=models.TextField(blank=True,null=True)
    about_image = models.ImageField(upload_to='major_celebration_historical_event/', blank=True, null=True)
    
    background = models.TextField(blank=True, null=True)
    background_ml = models.TextField(blank=True, null=True)
    background_hi = models.TextField(blank=True, null=True)
    background_image = models.ImageField(upload_to='major_celebration_historical_event/', blank=True, null=True)
    
    the_event = models.TextField(blank=True, null=True)
    the_event_ml = models.TextField(blank=True, null=True)
    the_event_hi = models.TextField(blank=True, null=True)
    the_event_image = models.ImageField(upload_to='major_celebration_historical_event/', blank=True, null=True)
    
    impact_and_significance = models.TextField(blank=True, null=True)
    impact_and_significance_ml = models.TextField(blank=True, null=True)
    impact_and_significance_hi = models.TextField(blank=True, null=True)
    impact_and_significance_image = models.ImageField(upload_to='major_celebration_historical_event/', blank=True, null=True)
    
    commemoration = models.TextField(blank=True, null=True)
    commemoration_ml = models.TextField(blank=True, null=True)
    commemoration_hi = models.TextField(blank=True, null=True)
    commemoration_image = models.ImageField(upload_to='major_celebration_historical_event/', blank=True, null=True)
    
    conclusion = models.TextField(blank=True, null=True)
    conclusion_ml = models.TextField(blank=True, null=True)
    conclusion_hi = models.TextField(blank=True, null=True)
    conclusion_image = models.ImageField(upload_to='major_celebration_historical_event/', blank=True, null=True)
    
    references = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=155)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='major_celebration_historical_event_likes', blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='major_celebration_historical_event_dislikes', blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.content_object}'


# # transation
# @receiver(post_save, sender=MajorCelebrationHistoricalEvent)
# def populate_translation_fields(sender, instance, created, **kwargs):
#     if created:
#         instance.about_en = translate_text(instance.about, 'en')  # Translate to English if necessary
#         instance.about_ml = translate_text(instance.about, 'ml')  # Translate to Malayalam
#         instance.about_hi = translate_text(instance.about, 'hi')  # Translate to Hindi
#         instance.save()  # Save the instance with populated translations