from django.contrib import admin

from .models import *

admin.site.register(Emotion)
admin.site.register(EmotionPack)
admin.site.register(EventTemplate)
admin.site.register(Vote)

@admin.action(description="Delete votes")
def delete_votes(modeladmin, request, queryset):
    Vote.objects.filter(event__in=queryset).delete()


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    actions = [
        delete_votes
    ]
