from django.contrib import admin
from .models import ChurchAndOtherBuilding,Person,MajorCelebrationHistoricalEvent,ChurchCommunity,InstitutionBuilding,Comment
admin.site.register(ChurchAndOtherBuilding)
admin.site.register(Person)
admin.site.register(MajorCelebrationHistoricalEvent)
admin.site.register(ChurchCommunity)
admin.site.register(InstitutionBuilding)
admin.site.register(Comment)
# Register your models here.
