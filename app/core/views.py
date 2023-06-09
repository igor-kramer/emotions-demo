from typing import Any, Dict
from django.db import models
from django.db.models.aggregates import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from core.forms import EventForm

from .models import EmotionPack, Event, Vote, Emotion

class EmotionPackList(LoginRequiredMixin, ListView):
    model = EmotionPack


class EmotionPackDetail(LoginRequiredMixin, DetailView):
    model = EmotionPack


class EventList(LoginRequiredMixin, ListView):
    model = Event

    def get_queryset(self):
        queryset = super().get_queryset().order_by('date', 'start_date')
        return queryset


class EventDetail(LoginRequiredMixin, DetailView):
    model = Event

    def get_queryset(self):
        queryset = super().get_queryset().filter(id=self.kwargs['pk'])
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        statistics = Emotion.objects.filter(vote__event=event).annotate(vote_count=Count('vote')).order_by('-vote_count')
        context['statistics'] = statistics
        return context
    

class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    success_url = '/events/'


class EventVote(DetailView):
    model = Event
    template_name = 'core/event_vote.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(id=self.kwargs['pk'])
        return queryset
        
    def post(self, request, pk):
        keys = request.POST.keys()
        emotion = [k for k in keys if '__.x' in k]
        if emotion:
            emotion = emotion[0].replace('emotion_', '').replace('__.x', '')
            _ = Vote.objects.create(event_id=pk, emotion_id=emotion)
        url = f"/vote/{ pk }/"
        return HttpResponseRedirect(url)