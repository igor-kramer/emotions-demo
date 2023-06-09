import uuid
from django.db import models


class EmotionPack(models.Model):
    title = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Emotion(models.Model):
    pack = models.ForeignKey(EmotionPack, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.title


class EventTemplate(models.Model):
    title = models.CharField(max_length=50)
    event_title = models.CharField(max_length=50)
    pack = models.ForeignKey(EmotionPack, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    template = models.ForeignKey(EventTemplate, verbose_name='Набор эмоций',on_delete=models.PROTECT, null=True)
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    date = models.DateField('Дата события')
    start_date = models.DateTimeField('Начало')
    end_date = models.DateTimeField('Окончание')

    def __str__(self):
        return self.title


class Vote(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    emotion = models.ForeignKey(Emotion, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{ self.event.title } { self.emotion.title }'
