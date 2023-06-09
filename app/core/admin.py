from django.contrib import admin

from .models import *

admin.site.register(Emotion)
admin.site.register(EmotionPack)
admin.site.register(Event)
admin.site.register(EventTemplate)
admin.site.register(Vote)
